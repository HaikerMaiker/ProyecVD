from django.urls import path
#from .views import index
from rest_framework import routers
from .views import LibrosViewSet, AutoresViewSet, GenerosViewSet, UsuariosViewSet, CalificacionesViewSet

#urlpatterns = [
#    path('',index,name="index")
#]

router = routers.DefaultRouter()
router.register('libros', LibrosViewSet)
router.register('autores', AutoresViewSet)
router.register('generos', GenerosViewSet)
router.register('usuarios', UsuariosViewSet)
router.register('calificaciones', CalificacionesViewSet)
urlpatterns = router.urls