from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data: dict) -> User:
        if self.context["request"].user.is_superuser == True:
            return User.objects.create_superuser(**validated_data)
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "is_superuser",
        ]
        read_only_fields = ["id", "is_superuser"]
        extra_kwargs = {
            "username": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="This field must be unique.",
                    )
                ]
            },
            "password": {"write_only": True},
            "email": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="This field must be unique.",
                    )
                ]
            },
        }

    def create(self, validated_data: dict) -> User:
        return User.objects.create_superuser(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
                continue
            setattr(instance, key, value)

        instance.save()

        return instance
