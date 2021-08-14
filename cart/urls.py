from django.urls import path
from cart.views import cart_detail ,add_in_cart , remove_from_cart

urlpatterns = [
    path('',cart_detail,name="cart_detils"),
    path('add/<int:product_id>',add_in_cart,name="add_in_cart"),
    path('remove/<int:product_id>',remove_from_cart,name="remove_from_cart"),
]