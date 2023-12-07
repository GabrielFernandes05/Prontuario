from django.contrib import admin
from .models import Medico, Paciente


class MedicoAdmin(admin.ModelAdmin):
    list_display = ("nome", "tel", "nascimento")


class PacienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "sintomas", "dataDeEntrada", "medicoResponsavel")


admin.site.register(Medico, MedicoAdmin)
admin.site.register(Paciente, PacienteAdmin)
