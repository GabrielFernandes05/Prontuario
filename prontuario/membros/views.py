from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import CadastroForm, LoginForm
from .models import Medico, Paciente
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def home(request):
    template = loader.get_template("home.html")
    c = 0
    for user in User.objects.all():
        c += 1
    context = {"c": c}
    return HttpResponse(template.render(context, request))


def cadastro(request):
    erro = False
    mensagem = "Usuário já cadastrado"
    template = loader.get_template("cadastro.html")
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data["user"]):
                erro = True
                print("Usuário já cadastrado", erro)
                if erro:
                    print(erro)
                context = {"form": form, "mensagem": mensagem, "erro": erro}
                return HttpResponse(template.render(context, request))
            else:
                user = form.cleaned_data["user"]
                password = form.cleaned_data["password"]
                nome = form.cleaned_data["nome"]
                tel = form.cleaned_data["tel"]
                nascimento = form.cleaned_data["nascimento"]
                medico = form.cleaned_data["medico"]
                if medico:
                    novoUsuario = Medico.objects.create_user(
                        username=user,
                        password=password,
                        nome=nome,
                        tel=tel,
                        nascimento=nascimento,
                    )
                    novoUsuario.save()
                    return HttpResponseRedirect("/login/")
                else:
                    novoUsuario = Paciente.objects.create_user(
                        username=user,
                        password=password,
                        nome=nome,
                        tel=tel,
                        nascimento=nascimento,
                    )
                    novoUsuario.save()
                    return HttpResponseRedirect("/login/")
    else:
        form = CadastroForm()
        context = {"form": form, "mensagem": mensagem, "erro": erro}
        return HttpResponse(template.render(context, request))


def login(request):
    erro = False
    mensagem = "Usuario ou senha estão incorretos!"
    template = loader.get_template("login.html")
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            nome_usuario = form.cleaned_data["user"]
            senha = form.cleaned_data["password"]
            usuario = authenticate(username=nome_usuario, password=senha)
            print(usuario)
            print(senha)
            if usuario != None:
                if Medico.objects.filter(username=usuario).exists():
                    print("logando como medico")
                    auth_login(request, usuario)
                    return HttpResponseRedirect("/medico/")
                elif Paciente.objects.filter(username=usuario).exists():
                    print("logando como paciente")
                    auth_login(request, usuario)
                    return HttpResponseRedirect("/paciente/")
            else:
                erro = True
                print("Usuario ou senha estão incorretos!", erro)
                return HttpResponse(
                    template.render(
                        {"form": form, "mensagem": mensagem, "erro": erro}, request
                    )
                )
    else:
        form = LoginForm()
    context = {"form": form, "mensagem": mensagem, "erro": erro}
    return HttpResponse(template.render(context, request))


@login_required
def medico(request):
    template = loader.get_template("medico.html")
    usera = False
    if request.user.is_authenticated:
        print("O usuário está autenticado")
        usera = True
    else:
        print("O usuário não está autenticado")
    return HttpResponse(template.render({"usera": usera}, request))


@login_required
def paciente(request):
    template = loader.get_template("paciente.html")
    usera = False
    if request.user.is_authenticated:
        print("O usuário está autenticado")
        usera = True
    else:
        print("O usuário não está autenticado")
    return HttpResponse(template.render({"usera": usera}, request))


def logout(request):
    request.session.flush()
    return HttpResponseRedirect("/")
