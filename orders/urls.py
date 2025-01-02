from django.urls import path

from .views import MyOrderView, CreateOrderItem

urlpatterns = [
    path("my-order", MyOrderView.as_view(), name="my_order"),
    path("add-product", CreateOrderItem.as_view(), name="add_product"),
]
