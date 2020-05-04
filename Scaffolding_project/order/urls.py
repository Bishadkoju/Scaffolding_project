from django.urls import path
from .views import *

urlpatterns=[path('sale/',make_sale,name='order_sale'),]
