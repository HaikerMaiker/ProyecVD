from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .models import Libro, Autor, Genero, Usuario, Calificacion
from .serializers import LibroSerializer, LibroGetSerializer, AutorSerializer, GeneroSerializer, UsuarioSerializer, CalificacionSerializer

# Create your views here.
#def index(request):
 #   return HttpResponse("Hola")

class LibrosViewSet(ModelViewSet):
    queryset= Libro.objects.all()
    #serializer
    #serializer_class = LibroSerializer
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return LibroGetSerializer
        return LibroSerializer


class AutoresViewSet(ModelViewSet):
    queryset= Autor.objects.all()
    #serializer
    serializer_class = AutorSerializer

class GenerosViewSet(ModelViewSet):
    queryset= Genero.objects.all()
    #serializer
    serializer_class = GeneroSerializer

class UsuariosViewSet(ModelViewSet):
    queryset= Usuario.objects.all()
    #serializer
    serializer_class = UsuarioSerializer

class CalificacionesViewSet(ModelViewSet):
    queryset= Calificacion.objects.all()
    #serializer
    serializer_class = CalificacionSerializer

