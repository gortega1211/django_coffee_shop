from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    description = models.TextField(max_length=300, verbose_name="Description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    available = models.BooleanField(default=True, verbose_name="Available")
    photo = models.ImageField(upload_to="logos", null=True, blank=True, verbose_name="Photo")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Create Date")
    update_date = models.DateTimeField(auto_now=True, verbose_name="Update Name")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
