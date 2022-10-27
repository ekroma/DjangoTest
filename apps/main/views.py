from rest_framework.generics import ListAPIView
from .models import Room, User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RoomRetrieve(serializers.ModelSerializer):
    pass


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

    def to_representation(self, instance:dict):
        res = super().to_representation(instance)
        res['users'] = UserSerializer(instance.users.all(), many=True).data
        return res


class RoomList(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    
#TODO: поиск студента по id и имени
