from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views 

app_name = 'apps.contenido'

# Importa la función eliminar_media desde tus vistas
from .views import eliminar_media

urlpatterns = [
    path('subir/', views.subir_media, name='subir_media'),
    path('ver/', views.ver_media, name='ver_media'),
    path('eliminar/<int:media_id>/', eliminar_media, name='eliminar_media'),  # Ajusta la ruta para aceptar media_id
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
