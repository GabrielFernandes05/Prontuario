from django.contrib.auth.models import User
from django.db import models

class Usuario(User):
    nome = models.CharField(max_length=255)
    tel = models.IntegerField()
    nascimento = models.DateField()
    medico = models.BooleanField()

    def __str__(self):
        return f"{self.nome}"

    def save(self, *args, **kwargs):
        self.medico = self.is_staff
        super().save(*args, **kwargs)

class Medico(Usuario):
    pass

class Paciente(Usuario):
    sintomas = models.CharField(max_length=255)
    dataDeEntrada = models.DateField()
    medicoResponsavel = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
