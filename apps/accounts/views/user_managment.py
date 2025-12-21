import json
from django.views import View
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from apps.accounts.models.user import User
from apps.accounts.forms.user_forms import UserForm


class UserManagementView(View):

    def get(self, request):
        user_id = request.GET.get("id")

        if user_id:
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                return JsonResponse({"error": "User not found"}, status=404)

            return JsonResponse({
                "data": model_to_dict(user, fields=["id", "email", "username", "phone", "role"])
            })

        users = list(
            User.objects.values("id", "email", "username", "phone", "role")
        )
        return JsonResponse({"data": users})

    def post(self, request):
        form = UserForm(request.POST)
        if not form.is_valid():
            return JsonResponse(form.errors, status=400)

        user = form.save()
        return JsonResponse({"message": "User created", "id": user.id}, status=201)

    def put(self, request):
        data = json.loads(request.body)
        user_id = data.get("id")

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)

        form = UserForm(data, instance=user)
        if not form.is_valid():
            return JsonResponse(form.errors, status=400)

        form.save()
        return JsonResponse({"message": "User updated"})

    def delete(self, request):
        data = json.loads(request.body)
        user_id = data.get("id")

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)

        user.delete()
        return JsonResponse({"message": "User deleted"})
