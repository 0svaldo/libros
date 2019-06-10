from django.contrib.auth.models import User, Group
from .models import Generos, Autores, Ubicacion, Libros
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class GenerosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Generos
        fields = ('genero',)

class AutoresSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Autores
        fields = ('nombre',)

class UbicacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ubicacion
        fields = ('ubicacion', 'comentarios',)

class LibrosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Libros
        fields = ('titulo', 'autor', 'genero',)
