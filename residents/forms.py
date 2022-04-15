from django.contrib.auth.forms import AuthenticationForm
from django.forms import TextInput, IntegerField, ModelForm
from .models import User


class CustomAuthForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(CustomAuthForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = TextInput(attrs={
            'id': 'floatingInput',
            'class': 'form-control',
            'name': 'username',
            'placeholder': 'login'})
        self.fields['password'].widget = TextInput(attrs={
            'type': 'password',
            'id': 'floatingPassword',
            'class': 'form-control',
            'name': 'password',
            'placeholder': 'Password'})


class CustomAuthWithCodeForm(ModelForm):

    class Meta:
        model = User

        fields = ['username', 'password', 'check_code']

    check_code = IntegerField(help_text="Enter your code")

    def __init__(self, *args, **kwargs):
        super(CustomAuthWithCodeForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = TextInput(attrs={
            'id': 'floatingInput',
            'class': 'form-control',
            'name': 'username',
            'placeholder': 'login'})
        self.fields['password'].widget = TextInput(attrs={
            'type': 'password',
            'id': 'floatingPassword',
            'class': 'form-control',
            'name': 'password',
            'placeholder': 'Password'})
        self.fields['check_code'].widget = TextInput(attrs={
            'type': 'password',
            'id': 'floatingCode',
            'class': 'form-control',
            'name': 'check_code',
            'placeholder': 'Code'})
