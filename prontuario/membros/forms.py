from django import forms


class CadastroForm(forms.Form):
    user = forms.CharField(label="Usuário", max_length=255)
    password = forms.CharField(label="Senha", max_length=255)
    nome = forms.CharField(label="Nome", max_length=255)
    tel = forms.IntegerField(label="Telefone")
    nascimento = forms.DateField(
        label="Data de nascimento", widget=forms.DateInput(attrs={"type": "date"})
    )
    medico = forms.BooleanField(label="Médico?", required=False)


class LoginForm(forms.Form):
    user = forms.CharField(label="Usuário", max_length=255)
    password = forms.CharField(label="Senha", max_length=255)
