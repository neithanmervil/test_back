#urls/app

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'usuario', views.UsuarioViewSet)
router.register(r'niveles', views.NivelViewSet)
router.register(r'puntuajes', views.PuntuajeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
