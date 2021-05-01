from django.contrib.auth.forms import UserCreationForm, UsernameField
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _


class RegisterForm(UserCreationForm):

    error_messages = {
        'password_mismatch': _('Пароли не совпадают'),
    }
    password1 = forms.CharField(
        label=_("Пароль"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=_("Пароль должен состоять минимум из 8 знаков и включать буквы"),
    )
    password2 = forms.CharField(
        label=_("Подтверждение пароля"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=_("Введите тот же пароль"),
    )

    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}
