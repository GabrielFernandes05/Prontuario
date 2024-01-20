from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models


class Usuario(User):
    nome = models.CharField(max_length=255, null=True)
    tel = models.IntegerField(null=True)
    nascimento = models.DateField(null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.nome}"


class Medico(Usuario):
    pass


class Paciente(Usuario):
    STATUS = [
        ("Na fila!", "Na fila!"),
        ("Em andamento!", "Em andamento!"),
        ("Finalizado!", "Finalizado"),
    ]

    sintomas = models.CharField(max_length=255, null=True)
    dataDeEntrada = models.DateField(null=True)
    medicoResponsavel = models.ForeignKey(Medico, on_delete=models.SET_NULL, null=True)
    doente = models.BooleanField(default=False, null=True)
    tratamento = models.CharField(max_length=255, null=True, default="Aguardando tratamento!")
    status = models.CharField(max_length=255, choices=STATUS, null=True, default="Na fila!")
    historicoTratamentos = models.JSONField(null=True, default=dict)

class UsuarioBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(username=username)
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
