from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *
# Create your views here.

# ViewSets
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsuarioSerializer


class NivelViewSet(viewsets.ModelViewSet):
    queryset = Nivel.objects.all()
    serializer_class = NivelSerializer
    permission_classes = [permissions.AllowAny]

class PuntuajeViewSet(viewsets.ModelViewSet):
    queryset = Puntuaje.objects.all()
    serializer_class = PuntuajeSerializer
    permission_classes = [permissions.AllowAny]
