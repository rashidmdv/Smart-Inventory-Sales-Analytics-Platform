from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.filters import SearchFilter, OrderingFilter
# from django_filters.rest_framework import DjangoFilterBackend

from apps.inventory.models import Product
from apps.inventory.serializers.product_serializer import ProductSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated]

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name", "sku"]
    ordering_fields = ["price", "stock", "created_at"]
    filterset_fields = ["is_active"]

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAdminUser()]
        return super().get_permissions()



from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

from apps.inventory.models import Product, InventoryTransaction
from apps.inventory.serializers.product_serializer import (
    InventoryTransactionSerializer,
)
from apps.inventory.services.inventory_service import InventoryService

class InventoryTransactionView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request):
        serializer = InventoryTransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product = serializer.validated_data["product"]
        txn_type = serializer.validated_data["transaction_type"]
        quantity = serializer.validated_data["quantity"]
        reference = serializer.validated_data.get("reference")

        InventoryService.process_transaction(
            product=product,
            txn_type=txn_type,
            quantity=quantity,
            reference=reference,
        )

        return Response(
            {"message": "Inventory updated successfully"},
            status=status.HTTP_201_CREATED,
        )

    def get(self, request):
        transactions = InventoryTransaction.objects.select_related("product")
        serializer = InventoryTransactionSerializer(transactions, many=True)
        return Response(serializer.data)

