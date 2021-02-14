"""

Cart Url conf.

This is the url configuration for the cart app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path(
        '<int:product_id>/add_to_cart', views.CartView.as_view(),
        name='add_to_cart'
    ),
]
