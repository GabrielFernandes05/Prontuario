from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("cadastro/", views.cadastro, name="cadastro"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("medico/", views.medico, name="medico"),
    path("paciente/", views.paciente, name="paciente"),
    path("medico/detalhes/<int:id>", views.detalhes, name="detalhes"),
    path("aceitarchamado/", views.aceitarchamado, name="aceitarchamado"),
    path("fecharchamado/", views.fecharchamado, name="fecharchamado"),
]
