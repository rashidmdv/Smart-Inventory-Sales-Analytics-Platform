from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.forms.models import model_to_dict

from apps.accounts.models.user import User
from apps.accounts.forms.user_forms import UserForm
from core.permissions.role_permission import IsAdmin
from core.helpers.pagination import StandardResultsPagination


class UserManagementView(APIView):
    # permission_classes = [IsAuthenticated, IsAdmin]
    # pagination_class = StandardResultsPagination

    def get(self, request):
        user_id = request.GET.get("id")

        if user_id:
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                return Response({"error": "User not found"}, status=404)

            return Response({
                "data": model_to_dict(user, fields=["id", "email", "username", "phone", "role"])
            })

        users = list(
            User.objects.values("id", "email", "username", "phone", "role")
        )
        return Response({"data": users})

    def post(self, request):
        form = UserForm(request.data)
        if not form.is_valid():
            return Response(form.errors, status=400)
        user = form.save()
        return Response({"message": "User created", "id": user.id}, status=201)

    def put(self, request):
        user_id = request.data.get("id")

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

        form = UserForm(request.data, instance=user)
        if not form.is_valid():
            return Response(form.errors, status=400)

        form.save()
        return Response({"message": "User updated"})

    def delete(self, request):
        user_id = request.data.get("id")

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

        user.delete()
        return Response({"message": "User deleted"})