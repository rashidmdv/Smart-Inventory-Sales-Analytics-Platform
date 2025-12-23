from rest_framework import serializers
from apps.inventory.models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("Stock cannot be negative")
        return value



from rest_framework import serializers
from apps.inventory.models import InventoryTransaction, Product

class InventoryTransactionSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source="product.name")

    class Meta:
        model = InventoryTransaction
        fields = "__all__"
        read_only_fields = ("id", "created_at")

    def validate(self, data):
        product = data["product"]
        qty = data["quantity"]
        txn_type = data["transaction_type"]

        if txn_type == "OUT" and product.stock < qty:
            raise serializers.ValidationError(
                "Insufficient stock for this product"
            )

        return data
