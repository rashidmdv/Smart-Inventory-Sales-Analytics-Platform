from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)
    sku = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2 ,null=True, blank=True)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    tax_percentage = models.IntegerField(max_length=3,default=0)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


class Inventory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)


class InventoryTransaction(models.Model):
    IN = "IN"
    OUT = "OUT"

    TRANSACTION_TYPE = [
        (IN, "Purchase / Stock In"),
        (OUT, "Sale / Stock Out"),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=3, choices=TRANSACTION_TYPE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.transaction_type} - {self.quantity}"
