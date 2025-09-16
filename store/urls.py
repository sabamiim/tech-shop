from shop.urls import urlpatterns
from store import views
from django.urls import path

urlpatterns = [
    path('cart/',views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),

]