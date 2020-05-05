from django.urls import path
from .views import *

urlpatterns=[path('sale/',make_sale,name='order_sale'),
             path('',OrderListView.as_view(),name='order_list'),
             path('<int:pk>/',OrderDetailView.as_view(),name='order_detail'),
             path('<int:pk>/approveQuotation/',approveQuotationView,name='order_approve_quotation'),
             path('<int:pk>/confirmOrder/',confirmOrderView,name='order_confirm'),
             path('<int:pk>/confirmPayment/',confirmPaymentView,name='order_payment_confirm'),
             path('<int:pk>/addDnCn/',addDnCnView,name='add_dn_cn'),
             ]
