from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from .models import Product
from .forms import ProductForm

class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"
    context_object_name = "products"

class ProductFormView(FormView):
    template_name="product_add.html"
    form_class = ProductForm
    success_url = reverse_lazy("product_list")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)