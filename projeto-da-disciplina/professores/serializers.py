from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Professor


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ["id", "nome", "email", "data_nascimento", "cpf"]
        read_only_fields = ["id"]
        extra_kwargs = {
            "email": {
                "validators": [
                    UniqueValidator(
                        queryset=Professor.objects.all(),
                        message="This field must be unique.",
                    )
                ]
            },
            "cpf": {
                "validators": [
                    UniqueValidator(
                        queryset=Professor.objects.all(),
                        message="This field must be unique.",
                    )
                ]
            },
        }

    def create(self, validated_data: dict) -> Professor:
        return Professor.objects.create(**validated_data)
