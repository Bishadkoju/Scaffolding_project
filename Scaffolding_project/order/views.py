from decimal import Decimal
from .filters import OrderFilter

from cart.cart import Cart
from django.shortcuts import render,get_object_or_404,redirect
from .models import *

from django.contrib import messages
from django.views import generic
from .forms import *


def make_sale(request):
    mode='sale'
    cart=Cart(request)
    context={'cart':cart,'mode':mode}

    if request.POST:
        total_price=0
        for items in cart:
            total_price +=items['total_price']
        order_summary=OrderRegister(total_price=total_price,user=request.user)
        order_summary.save()
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
            order.total_price=order.total_price-order.discount_amount
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
            order.status='ORDER CONFIRMED'
            order.save()
            messages.success(request,' Order Confirmed ')
            return redirect('order_detail',pk=order.pk)

    context={'order':order,}
    return render(request,'order/order_confirm.html',context)

def confirmPaymentView(request,pk):
    order=get_object_or_404(OrderRegister,pk=pk)
    form=PaymentConfirmForm()
    if request.method=='POST':
        form=PaymentConfirmForm(request.POST)
        if form.is_valid():
            order.payment_amount=form.cleaned_data['payment_amount']
            order.status=' ORDER PACKING '
            order.save()
            messages.success(request,'Payment Confirmed. Your order is now Packing')
            return redirect('order_detail',pk=order.pk)
    context={'order':order,'form':form}
    return render (request,'order/order_payment_confirm.html',context)


def addDnCnView(request,pk):
    order=get_object_or_404(OrderRegister,pk=pk)
    form=DnCnForm()
    if request.method=='POST':
        print('pasted')
        form=DnCnForm(request.POST)
        if form.is_valid():
            info=DnCnRegister()
            info.order_register=order
            info.type=form.cleaned_data['type']
            info.truck_rate=form.cleaned_data['truck_rate']
            info.truck_type=form.cleaned_data['truck_type']
            info.truck_plate_num=form.cleaned_data['truck_plate_num']
            info.remarks=form.cleaned_data['remarks']
            info.recorded_by=request.user
            info.save()
            order.status='ORDER SHIPPED'
            order.save()
            messages.success(request,"Note added")
            return redirect('order_detail',pk=order.pk)

    context={'order':order,'form':form}
    return render(request,'order/add_Dn_Cn.html',context)
