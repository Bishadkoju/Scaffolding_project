from django.shortcuts import render,redirect
from django.views import generic
from .models import ProductRegister
from .forms import addProductForm
from django.urls import reverse_lazy,reverse
from .filters import ProductFilter
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin 
from django.contrib import messages

# Create your views here.

class ProductCreate(SuccessMessageMixin,generic.CreateView):
    model=ProductRegister
    template_name='product/product_add.html'
    form_class=addProductForm
    success_url=reverse_lazy('dashboard')
    success_message="Product added Successully !!"
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['action']='Add'
        context['title']='Add Product'
        return context

class ProductUpdateView(SuccessMessageMixin,generic.UpdateView):
    model=ProductRegister
    form_class=addProductForm
    template_name='product/product_add.html'
    success_message="Product Updated Successfully"
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['action']='Update'
        context['title']='Update Product'
        return context


class ProductListView(generic.ListView):
    model=ProductRegister
    paginate_by=10
    context_object_name='product_list'
    template_name='product/product_list.html'

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['filter']=ProductFilter(self.request.GET,self.get_queryset())
        return context

class ProductDetailView(generic.DetailView):
    model=ProductRegister
    context_object_name='product'
    template_name='product/product_detail.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['action']='Detail'
        context['title']='Product Detail'
        return context
   
class ProductDeleteView(SuccessMessageMixin,generic.DeleteView):
    model=ProductRegister
    context_object_name='product'
    template_name='product/product_detail.html'
    success_message="Product Deleted Successfully"
    success_url=reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['action']='Delete'
        context['title']='Delete Product'
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)






