from django.db import models
import uuid


class Professor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11, unique=True)

    # disciplinas = models.ManyToManyField(
    #     "disciplinas.Disciplina", related_name="professores"
    # )
