from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views

from .views import CustomPasswordChangeDoneView
from apps.contenido import views


urlpatterns = [
    path('admin/', admin.site.urls),
     path('cambiar-contraseña/', auth_views.PasswordChangeView.as_view(), name='cambiar_contraseña'),
    path('password_change_done/', CustomPasswordChangeDoneView.as_view(), name='password_change_done'),
    path('', views.ver_media, name='inicio'),  # Esta es la modificación para redirigir a ver_media
    # path('', inicio, name='inicio'),
    path('usuario/', include('apps.usuarios.urls')),
    path('carga_archivos/', include('apps.carga_archivos.urls')),
    path('contenido/', include('apps.contenido.urls')),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
