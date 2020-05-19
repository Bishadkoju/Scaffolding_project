from django.urls import include,path
from .views import *
from django.views.generic import RedirectView

urlpatterns=[
    path('product/',include('product.urls')),
    path('dashboard/',dashboard,name='dashboard'),
    path('account/',include('account.urls')),
    path('',RedirectView.as_view(url='dashboard/')),
    path('supplier/',include('supplier.urls')),
    path('project/',include('project.urls')),
    path('cart/',include('cart.urls')),
    path('order/',include('order.urls')),
    path('company/add',CompanyCreateView.as_view(),name='company_add'),
    path('company/<int:pk>/update',CompanyUpdateView.as_view(),name='company_update'),
    path('company/',CompanyListView.as_view(),name='company_list'),
    path('company/<int:pk>/',CompanyDetailView.as_view(),name='company_detail'),
    path('company/<int:pk>/delete',CompanyDeleteView.as_view(),name='company_delete'),
    
    ]
