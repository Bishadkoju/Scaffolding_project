from django.shortcuts import render,get_object_or_404,redirect
from decimal import Decimal
from product.models import ProductRegister
from django.conf import settings
from.cart import Cart
from django.http import HttpResponseNotFound,Http404

# Create your views here.

def cartView(request,mode):
    product_list=ProductRegister.objects.all()
    cart=Cart(request)
    modes=['sale','purchase','rent']
    if mode not in modes:
        raise Http404
    context={'mode':mode,}
    print(mode)

    if request.GET:
        if request.GET['action']=='add':
            product_id=request.GET['id']
            product = get_object_or_404(ProductRegister, id=product_id)
            cart.add(product=product)
            return redirect('cart_view',mode=mode)
        
        if request.GET['action']=='remove':
            product_id=request.GET['id']
            product = get_object_or_404(ProductRegister, id=product_id)
            cart.remove(product=product)
            return redirect('cart_view',mode=mode)

        if request.GET['action']=='clear':
            cart.clear()
            return redirect('cart_view',mode=mode)


    if request.POST:
        if request.POST['submit']=='update':
            product_ids=cart.cart.keys()
            for product_id in product_ids:
                update_value=int(request.POST[product_id])
                cart.update(product_id=product_id,update_value=update_value)
            return redirect('cart_view',mode=mode)

        if request.POST['submit']=='checkout':
            if mode=='sale':
                return redirect('order_sale')
    
    context['product_list']=product_list
    context['cart']=cart
    return render(request,'cart/cart_view.html',context)
