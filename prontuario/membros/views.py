from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import CadastroForm, LoginForm
from .models import Medico, Paciente
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())


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
                if usuario in Medico.objects.all():
                    print("logando como medico")
                    login(request, usuario)
                    return HttpResponseRedirect("/medico/")
                elif usuario in Paciente.objects.all():
                    print("logando como paciente")
                    login(request, usuario)
                    return HttpResponseRedirect("/paciente/")
    else:
        form = LoginForm()
    context = {"form": form}
    return HttpResponse(template.render(context, request))



def medico(request):
    template = loader.get_template("medico.html")
    return HttpResponse(template.render())



def paciente(request):
    template = loader.get_template("paciente.html")
    return HttpResponse(template.render())



def logout(request):
    request.session.flush()
    return HttpResponseRedirect("/")
