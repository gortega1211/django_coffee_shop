from django.urls import path

from .views import ProductListView, ProductFormView

urlpatterns = [
    path('', ProductListView.as_view(), name="product_list"),
    path('add/', ProductFormView.as_view(), name="product_add")
]
