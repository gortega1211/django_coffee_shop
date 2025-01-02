from django import forms

from .models import Product


class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, label="Name", widget=forms.TextInput(attrs={"class": "form-control"}))
    description = forms.CharField(max_length=300, label="Description", widget=forms.TextInput(attrs={"class": "form-control"}))
    price = forms.DecimalField(max_digits=10, decimal_places=2, label="Price", widget=forms.NumberInput(attrs={"class": "form-control"}))
    available = forms.BooleanField(initial=True, label="Available", widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
    photo = forms.ImageField(label="Photo", required=False, widget=forms.FileInput(attrs={"class": "form-control"}))

    def save(self):
        Product.objects.create(
            name=self.cleaned_data["name"],
            description=self.cleaned_data["description"],
            price=self.cleaned_data["price"],
            available=self.cleaned_data["available"],
            photo=self.cleaned_data["photo"],
        )
