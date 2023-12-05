from django.contrib import admin
from .models import Usuario, Medico, Paciente


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("user", "password", "nome", "tel", "nascimento", "medico")


class MedicoAdmin(admin.ModelAdmin):
    list_display = ("nome", "medico", "usuario_ptr")


class PacienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "sintomas", "dataDeEntrada", "medicoResponsavel", "medico")


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Medico, MedicoAdmin)
admin.site.register(Paciente, PacienteAdmin)
