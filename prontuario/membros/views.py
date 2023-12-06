from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from .models import Usuario, Medico, Paciente
from .forms import CadastroForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())


def cadastro(request):
    template = loader.get_template("cadastro.html")
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            try:
                usuario_aux = User.objects.get(user=form.cleaned_data["user"])
                if usuario_aux:
                    print("Usuário já existe")
                    return HttpResponseRedirect("/cadastro/")
            except User.DoesNotExist:
                user = form.cleaned_data["user"]
                password = form.cleaned_data["password"]
                nome = form.cleaned_data["nome"]
                tel = form.cleaned_data["tel"]
                nascimento = form.cleaned_data["nascimento"]
                medico = form.cleaned_data["medico"]
                novoUsuario = User.objects.create_user(user=user, password=password, nome=nome, tel=tel, nascimento=nascimento, medico=medico)
                novoUsuario.save()
                return HttpResponseRedirect("/login/")
    else:
        form = CadastroForm()
        context = {"form": form}
        return HttpResponse(template.render(context, request))


def login(request):
    template = loader.get_template("login.html")
    return HttpResponse(template.render())


@login_required
def medico(request):
    template = loader.get_template("medico.html")
    return HttpResponse(template.render())


@login_required
def paciente(request):
    template = loader.get_template("paciente.html")
    return HttpResponse(template.render())


@login_required
def logout(request):
    request.session.flush()
    return HttpResponseRedirect("/")
