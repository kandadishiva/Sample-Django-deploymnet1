from django.urls import path
from . import views

print(3)
urlpatterns=[
    path('',views.home, name='home'),
    path('add',views.add, name='add'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('products',views.products, name='products'),
    path('customers/<str:cid>/',views.customers,name='customers'),
]