from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from .models import Usuario, Medico, Paciente
from .forms import CadastroForm, LoginForm


def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render())


def cadastro(request):
    template = loader.get_template("cadastro.html")
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data["user"]
            if Usuario.objects.filter(user=user).exists() != True:
                password = form.cleaned_data["password"]
                nome = form.cleaned_data["nome"]
                tel = form.cleaned_data["tel"]
                nascimento = form.cleaned_data["nascimento"]
                medico = form.cleaned_data["medico"]
                if medico:
                    usuario = Medico(
                        user=user,
                        password=password,
                        nome=nome,
                        tel=tel,
                        nascimento=nascimento,
                    )
                    usuario.save()
                else:
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
                return HttpResponse("Usuário já cadastrado")
    else:
        form = CadastroForm()
        context = {"form": form}
        return HttpResponse(template.render(context, request))


def login(request):
    template = loader.get_template("login.html")
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data["user"]
            password = form.cleaned_data["password"]
            if Usuario.objects.filter(user=user).exists() == True:
                for x in range(0, (len(Usuario.objects.all()))):
                    i = Usuario.objects.all()[x]
                    if i.user == user:
                        if i.password == password:
                            if i.medico:
                                return HttpResponseRedirect("/medico/")
                            else:
                                return HttpResponseRedirect("/paciente/")
                        else:
                            return HttpResponse("Senha incorreta!")
            else:
                return HttpResponse("Usuário não cadastrado")
            return HttpResponseRedirect("/")
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