from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Product
from .forms import ProductForm
from .serializers import ProductSerializer


class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.filter(available=True)

class ProductFormView(FormView):
    template_name = "product_add.html"
    form_class = ProductForm
    success_url = reverse_lazy("product_list")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProductListAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )
