from django.shortcuts import render
# from django.contrib.auth.models import User
from messenger.models import User # так как использую кастомную форму User импортировать надо из моделей в messenger
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'