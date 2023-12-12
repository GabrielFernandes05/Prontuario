from .forms import CadastroForm, LoginForm, CriarChamadoForm, CancelarChamadoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
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
    lista_de_pacientes = []
    for x in Paciente.objects.all():
        print(x.username, x.medicoResponsavel)
        lista_de_pacientes.append(x)
    if request.user.is_authenticated:
        print("O usuário está autenticado")
        usera = True
        medico = False
        username = request.user.username
        user = request.user
        print(username)
        if Medico.objects.all().filter(username=username).exists():
            medico = True
            print(medico)
        nome = "0"
        for x in Medico.objects.all():
            if x.username == username:
                nome = x.nome
                print(nome)
                break
        for x in Paciente.objects.all():
            if str(x.medicoResponsavel) == str(nome):
                print("achei!")
                print(x.medicoResponsavel, nome)
    else:
        print("O usuário não está autenticado")
    return HttpResponse(
        template.render(
            {
                "usera": usera,
                "lista_de_pacientes": lista_de_pacientes,
                "medico": medico,
                "nome": nome,
            },
            request,
        )
    )


@login_required
def paciente(request):
    template = loader.get_template("paciente.html")
    usera = False
    medico = False
    for x in Medico.objects.all():
        if x.username == request.user.username:
            medico = True
    if request.method == "POST":
        form = CriarChamadoForm(request.POST)
        if form.is_valid():
            sintoma = form.cleaned_data["sintomas"]
            data = form.cleaned_data["dataDeEntrada"]
            usuario = request.user.username
            print(usuario)
            c = 0
            if medico == False:
                for x in Paciente.objects.all():
                    if x.username == usuario:
                        break
                    else:
                        c += 1
                usuario = Paciente.objects.all()[c]
                usuario.sintomas = sintoma
                usuario.dataDeEntrada = data
                usuario.doente = True
                usuario.save()
    else:
        form = CriarChamadoForm()
    if request.method == "POST":
        form2 = CancelarChamadoForm(request.POST)
        if form2.is_valid():
            username = request.user.username
            c = 0
            for x in Paciente.objects.all():
                if x.username == username:
                    break
                else:
                    c += 1
            paciente = Paciente.objects.all()[c]
            paciente.doente = False
            paciente.sintomas = ""
            paciente.dataDeEntrada = None
            paciente.medicoResponsavel = None
            paciente.save()
    else:
        form2 = CancelarChamadoForm()
    if request.user.is_authenticated:
        print("O usuário está autenticado")
        usera = True
        username = request.user.username
        if medico == False:
            c = 0
            for x in Paciente.objects.all():
                if x.username == username:
                    break
                else:
                    c += 1
            paciente = Paciente.objects.all()[c]
            doente = paciente.doente
            sintoma = paciente.sintomas
            data = paciente.dataDeEntrada
            nome = paciente.nome
            medicoResponsavel = paciente.medicoResponsavel
            medicoResponsavel = str(medicoResponsavel)
            if medicoResponsavel == "None":
                medicoResponsavel = "Na fila..."
            else:
                medicoResponsavel = f"Dr.{medicoResponsavel.capitalize()}"
        else:
            doente = 0
            sintoma = 0
            data = 0
            medicoResponsavel = 0
            nome = 0
    else:
        print("O usuário não está autenticado")
    return HttpResponse(
        template.render(
            {
                "usera": usera,
                "medico": medico,
                "form": form,
                "form2": form2,
                "doente": doente,
                "sintoma": sintoma,
                "data": data,
                "nome": nome,
                "medicoResponsavel": medicoResponsavel,
            },
            request,
        )
    )


def logout(request):
    request.session.flush()
    return HttpResponseRedirect("/")


@login_required
def detalhes(request, id):
    template = loader.get_template("detalhes.html")
    x = Paciente.objects.get(id=id)
    username = request.user.username
    medico = False
    for x in Medico.objects.all():
        if x.username == username:
            medico = True
    context = {
        "x": x,
        "medico": medico,
    }
    return HttpResponse(template.render(context, request))
