from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('cart_list/', views.cart_list, name='cart_list'),
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('full_remove/<int:product_id>/', views.full_remove, name='full_remove'),
]