from django.db import models
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from messenger.models import User # так как использую кастомную форму User импортировать надо из моделей в messenger
from django import forms


class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    first_name = forms.CharField(label = "Имя")
    last_name = forms.CharField(label = "Фамилия")

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2", )

