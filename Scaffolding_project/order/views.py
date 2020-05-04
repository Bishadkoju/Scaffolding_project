from cart.cart import Cart
from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from decimal import Decimal
from django.contrib import messages


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
                                          quantity=items['quantity'])
            order_item.save() 
        cart.clear()
        messages.success(request,'Order Registered successfully ')
        return redirect('dashboard')

    return render(request,'order/order_sale.html',context)