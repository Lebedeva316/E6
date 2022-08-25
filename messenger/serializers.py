from rest_framework import serializers
from .models import User, Room, Message


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
       model = User
       fields = ('username', 'about')




class RoomSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Room
        fields = ('name', 'date', 'roomUsers')



class MessageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'