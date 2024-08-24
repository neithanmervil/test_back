from rest_framework import serializers
from .models import Usuario, Nivel, Puntuaje

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'  # Incluye el campo 'id'

class NivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nivel
        fields = '__all__' # Incluye el campo 'id'

class PuntuajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puntuaje
        fields ='__all__'  # Incluye el campo 'id'
