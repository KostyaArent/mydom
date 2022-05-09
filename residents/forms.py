from django.contrib.auth.forms import AuthenticationForm
from django.forms import TextInput, IntegerField, ModelForm, Select, FileInput

from django.forms.models import inlineformset_factory

from .models import User, Appeal, Own, AppealPicture


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
            'placeholder': 'login',
            'readonly':'readonly'})
        self.fields['password'].widget = TextInput(attrs={
            'type': 'password',
            'id': 'floatingPassword',
            'class': 'form-control',
            'name': 'password',
            'placeholder': 'Password',
            'readonly':'readonly'})
        self.fields['check_code'].widget = TextInput(attrs={
            'type': 'password',
            'id': 'floatingCode',
            'class': 'form-control',
            'name': 'check_code',
            'placeholder': 'Code'})


class AppealForm(ModelForm):

    class Meta:
        model = Appeal
        fields = ['category', 'address', 'text']

    def __init__(self, *args, **kwargs):
        super(AppealForm, self).__init__(*args, **kwargs)
        addresses = Own.objects.all()
        self.fields['category'].widget = Select(
            attrs={
                'class': 'form-select mb-3',
            },
            choices=Appeal.CATEGORIES
            )
        self.fields['address'].widget = Select(
            attrs={
                'class': 'form-select mb-3',
            },
            choices=[(c.id, f'{c.house}, {c.number}') for c in addresses]
            )
        self.fields['text'].widget = TextInput(attrs={
            'class': 'form-control',
            })


class AppealImageForm(ModelForm):

    class Meta:
        model = AppealPicture
        fields = ['image']

    def __init__(self, *args, **kwargs):
        super(AppealImageForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget = FileInput(attrs={
            'type': 'file',
            'id': 'formFile',
            'placeholder': 'Photo',
            'class': 'form-control'
            })

ImageFormset = inlineformset_factory(
    Appeal, AppealPicture, form = AppealImageForm,
    fields='__all__', extra=3, can_delete=False
    )
