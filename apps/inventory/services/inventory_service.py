from django.db import transaction
from apps.inventory.models import InventoryTransaction, Product

class InventoryService:

    @staticmethod
    @transaction.atomic
    def process_transaction(product, txn_type, quantity, reference=None):

        if txn_type == "IN":
            product.stock += quantity
        elif txn_type == "OUT":
            if product.stock < quantity:
                raise ValueError("Insufficient stock")
            product.stock -= quantity

        product.save()

        InventoryTransaction.objects.create(
            product=product,
            transaction_type=txn_type,
            quantity=quantity,
            reference=reference,
        )

        return product
