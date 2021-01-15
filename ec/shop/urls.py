from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('list/', views.ShopList.as_view(), name='shop_list'),
    path('detail/<int:pk>/', views.ProductDetail.as_view(),
         name='product_detail'),
    path('create/', views.new_product, name='product_create'),
    path('delete/<int:pk>/', views.ProductDelete.as_view(),
         name='product_delete'),
]
