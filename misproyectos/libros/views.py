from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .models import Generos, Autores, Ubicacion, Libros
from .serializers import UserSerializer, GroupSerializer, AutoresSerializer 
from .serializers import GenerosSerializer, UbicacionSerializer, LibrosSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class AutoresViewSet(viewsets.ModelViewSet):
    """
    API endpoint para visualizar autores
    """
    queryset = Autores.objects.all()
    serializer_class = AutoresSerializer

class GenerosViewSet(viewsets.ModelViewSet):
    """
    API endpoint para visualizar generos
    """
    queryset = Generos.objects.all()
    serializer_class = GenerosSerializer

class UbicacionViewSet(viewsets.ModelViewSet):
    """
    API endpoint para visualizar generos
    """
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer

class LibrosViewSet(viewsets.ModelViewSet):
    """
    API endpoint para visualizar libros
    """
    queryset = Libros.objects.all()
    serializer_class = LibrosSerializer



