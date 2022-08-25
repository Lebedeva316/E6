from django.forms import ModelForm
from .models import User, Room

class UserEditForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'about', 'avatar']


class RoomCreatedForm(ModelForm):

    class Meta:
        model = Room
        fields = ['name', 'roomUsers']