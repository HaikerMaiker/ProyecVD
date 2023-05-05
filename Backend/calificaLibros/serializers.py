from rest_framework.serializers import ModelSerializer, ALL_FIELDS
from .models import Libro, Autor, Genero, Usuario, Calificacion

class LibroSerializer(ModelSerializer):
    class Meta:
        model = Libro
        fields = ALL_FIELDS


class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = ALL_FIELDS

class GeneroSerializer(ModelSerializer):
    class Meta:
        model = Genero
        fields = ALL_FIELDS

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ALL_FIELDS

class CalificacionSerializer(ModelSerializer):
    class Meta:
        model = Calificacion
        fields = ALL_FIELDS

class LibroGetSerializer(ModelSerializer):
    genero = GeneroSerializer()
    autores = AutorSerializer(many = True)
    calificaciones = CalificacionSerializer(many=True, required = False)
    class Meta:
        model = Libro
        fields = ALL_FIELDS
    