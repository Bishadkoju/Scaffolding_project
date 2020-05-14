from decimal import Decimal
from .filters import OrderFilter
from project.models import ProjectRegister

from cart.cart import Cart
from django.shortcuts import render,get_object_or_404,redirect
from django.http.response import Http404,HttpResponseBadRequest
from .models import *

from django.contrib import messages
from django.views import generic
from .forms import *


def quotation_confirm(request,mode):
    cart=Cart(request,mode)
    context={'cart':cart,'mode':mode}
    print(context['mode'])
    if mode =='Rent':
        rent_form=RentConfirmForm()
        context['rent_form']=rent_form

    if request.POST:
        if mode == 'Rent':
            rent_form=RentConfirmForm(request.POST)
            if rent_form.is_valid():
                duration=rent_form.cleaned_data['expected_duration']
                rent_form.cleaned_data['returned_date']=None
        total_price=0
        for items in cart:
            total_price +=items['total_price']

        order_summary=OrderRegister(total_price=total_price,
                                    payment_total=total_price,
                                    user=request.user,
                                    type=mode)
        order_summary.save()

        if mode=='Rent':
            order_summary.total_price=total_price*duration
            order_summary.save()
            rent_detail=rent_form.save(commit=False)
            rent_detail.order_register=order_summary
            rent_detail.save()


        
        for items in cart:
            order_item=OrderItemsRegister(order_register=order_summary,
                                          product=items['product'],
                                          product_price=items['price'],
                                          quantity=items['quantity'],
                                          sub_total=items['price']*items['quantity'])
            order_item.save() 
        cart.clear()
        messages.success(request,'Order Registered successfully ')
        return redirect('order_detail',pk=order_summary.pk)

    return render(request,'order/order_sale.html',context)


class OrderListView(generic.ListView):
    model=OrderRegister
    paginate_by=10
    context_object_name='order_list'
    template_name='order/order_list.html'


    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['filter']=OrderFilter(self.request.GET,self.get_queryset())
        return context

class OrderDetailView(generic.DetailView):
    model=OrderRegister
    context_object_name='order'
    template_name='order/order_view.html'


  

def approveQuotationView(request,pk):
    order=get_object_or_404(OrderRegister,pk=pk)
    if request.method=='POST':
        form=ApproveQuotationForm(request.POST)
        if form.is_valid():
            order.payment_advance=form.cleaned_data['payment_advance']
            order.discount_rate=form.cleaned_data['discount_rate']
            order.discount_amount=order.discount_rate*order.total_price/100
            order.payment_total=order.total_price-order.discount_amount
            order.status='QUOTATION APPROVED'
            order.save()
            messages.success(request,"Quotation Approved")
            return redirect('order_detail',pk=order.pk)
    else:
        form=ApproveQuotationForm()
        context={'form':form,'order':order,}

    return render(request,'order/order_approve_quotation.html',context)

def confirmOrderView(request,pk):
    order=get_object_or_404(OrderRegister,pk=pk)
    if request.method=='POST':
        if request.POST['submit']=='confirm':
            form=ConfirmOrderForm(request.POST)
            
            if form.is_valid():
                order.project=get_object_or_404(ProjectRegister,pk=form.cleaned_data['project'].id)
                
                order.status='ORDER CONFIRMED'
                order.payment_due=order.payment_total-order.payment_received
                order.save()

                order.project.payment_total=order.payment_total
                order.project.payment_due=order.payment_due
                order.project.payment_received=order.payment_received
                order.project.save()

                messages.success(request,' Order Confirmed ')
                return redirect('order_detail',pk=order.pk)
    else:
        form=ConfirmOrderForm()
        form.fields['project'].queryset=ProjectRegister.objects.filter(company=request.user.profile.company)
        


    context={'order':order,'form':form}
    return render(request,'order/order_confirm.html',context)

def confirmPaymentView(request,pk):
    order=get_object_or_404(OrderRegister,pk=pk)
    form=PaymentConfirmForm()
    if request.method=='POST':
        form=PaymentConfirmForm(request.POST)
        if form.is_valid():
            order.payment_received+=form.cleaned_data['payment_received']
            order.payment_due=order.payment_total-order.payment_received
            order.status=' ORDER PACKING '
            order.save()
            messages.success(request,'Payment Confirmed. Your order is now Packing')
            return redirect('order_detail',pk=order.pk)
    context={'order':order,'form':form}
    return render (request,'order/order_payment_confirm.html',context)


def addDnCnView(request,pk,type):
    order=get_object_or_404(OrderRegister,pk=pk)
    if type not in ('DN','CN'):
        raise Http404
    if type =='DN':
        title='Delivery Note'
    else:
        if order.type !='Rent':
            raise Http404('Collection Note cannot be added ')
        title='Collection Note'

    DnCn=order.dncnregister_set.filter(type=type)
    if DnCn.count()>0:
        raise Http404(f'{title} already added')
    context={'order':order,'title':title}

    
    if request.method=='POST':
        form=DnCnForm(request.POST)
        if form.is_valid() :
            print(order.type)
            if order.type == 'Rent':
                rent_detail=RentalDetails.objects.get(id=order.rentaldetails.id)
                if type == 'DN':       
                    rent_detail.ordered_date=request.POST['date']
                    rent_detail.save()
                else:
                    rent_detail.returned_date=request.POST['date']
                    rent_detail.save()
                    

            info=form.save(commit=False)
            info.order_register=order
            info.type=type
            info.recorded_by=request.user

            if order.type=='Rent' and type=='CN':
                order.status='ORDER RETURNED'
            else :
                order.status='ORDER SHIPPED'


            info.save()
            
            order.save()
            messages.success(request,"Note added")
            return redirect('order_detail',pk=order.pk)
    else:
        form=DnCnForm()

    context['form']=form
    return render(request,'order/add_Dn_Cn.html',context)


