from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from .models import Usuario, Medico, Paciente
from .forms import CadastroForm


def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())


def cadastro(request):
    template = loader.get_template("cadastro.html")
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data["user"]
            password = form.cleaned_data["password"]
            nome = form.cleaned_data["nome"]
            tel = form.cleaned_data["tel"]
            nascimento = form.cleaned_data["nascimento"]
            medico = form.cleaned_data["medico"]
            if medico:
                usuario = Medico(
                    user=user,
                    nome=nome,
                    tel=tel,
                    nascimento=nascimento,
                )
                usuario.save()
            usuarioGeral = Usuario(
                user=user,
                password=password,
                nome=nome,
                tel=tel,
                nascimento=nascimento,
                medico=medico,
            )
            usuarioGeral.save()
            return HttpResponseRedirect("/login/")
    else:
        form = CadastroForm()
        context = {"form": form}
        return HttpResponse(template.render(context, request))


def login(request):
    template = loader.get_template("login.html")
    return HttpResponse(template.render())
