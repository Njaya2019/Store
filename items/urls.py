"""

Customers Url conf.

This is the url configuration for the customers app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path(
        'add_product', views.Products.as_view(), name='add_product'
    ),
]