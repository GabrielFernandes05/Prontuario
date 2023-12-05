from django.db import models


class Usuario(
    models.Model
):  # user = Usuario(user="user", password="password", nome="nome", tel=123456789, nascimento="2000-01-01", medico=False)
    user = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    nome = models.CharField(max_length=255)
    tel = models.IntegerField()
    nascimento = models.DateField()
    medico = models.BooleanField()

    def __str__(self):
        return f"{self.nome}"


class Medico(Usuario):
    usuario_ptr = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        parent_link=True,
        related_name="medico_usuario",
    )

    def save(self, *args, **kwargs):
        self.medico = True
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome}"


class Paciente(Usuario):
    sintomas = models.CharField(max_length=255)
    dataDeEntrada = models.DateField()
    medicoResponsavel = models.ForeignKey(Medico, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        self.medico = False
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome}"
