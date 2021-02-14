"""

Orders Url conf.

This is the url configuration for the order app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path(
        'make_order', views.OrdersView.as_view(),
        name='the_order'
    ),
]
