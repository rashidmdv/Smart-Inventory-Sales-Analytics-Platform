from apps.accounts.models import User


def register_user(validated_data):
    password = validated_data.pop("password")
    return User.objects.create_user(password=password, **validated_data)
