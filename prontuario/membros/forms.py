from django import forms

class CadastroForm(forms.Form):
    user = forms.CharField(label="Usuário", max_length=255,required=True)
    password = forms.CharField(label="Senha", max_length=255,required=True)
    nome = forms.CharField(label="Nome", max_length=255,required=True)
    tel = forms.IntegerField(label="Telefone",required=True)
    nascimento = forms.DateField(
        label="Data de nascimento", widget=forms.DateInput(attrs={"type": "date"})
    ,required=True)
    medico = forms.BooleanField(label="Médico?", required=False)


class LoginForm(forms.Form):
    user = forms.CharField(label="Usuário", max_length=255)
    password = forms.CharField(label="Senha", max_length=255)

class CriarChamadoForm(forms.Form):
    sintomas = forms.CharField(label="Escreva seus sintomas", max_length=255, required=True)
    dataDeEntrada = forms.DateField(label="Data do chamado", widget=forms.DateInput(attrs={"type": "date"})
    ,required=True)

class CancelarChamadoForm(forms.Form):
    cancelar = forms.BooleanField(label="Entendo que estou cancelando meu chamado!", required=True)