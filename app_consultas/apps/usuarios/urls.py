from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LoginView, LogoutView

from .views import RegistrarUsuario, ListarUsuarios, EliminarUsuario


app_name = 'apps.usuarios'

urlpatterns = [
   
    path("registrar/", RegistrarUsuario.as_view(), name='registrar'),
    path("iniciar_sesion/", LoginView.as_view(template_name="usuarios/iniciar_sesion.html"), name= 'iniciar_sesion'),
    path("cerrar_sesion/", LogoutView.as_view(), name='cerrar_sesion'),
    path('listar_usuarios/', ListarUsuarios, name='listar_usuarios'),
    path("eliminar_usuario/<int:pk>", EliminarUsuario.as_view(), name='eliminar_usuario'), 

   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)