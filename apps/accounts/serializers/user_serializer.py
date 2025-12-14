from rest_framework import serializers
from ..models.user import User


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
            "phone",
            "name"
        )


    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value

    # def create(self, validated_data):
    #     password = validated_data.pop("password")
    #     user = User.objects.create_user(
    #         password=password,
    #         **validated_data
    #     )
    #     return user