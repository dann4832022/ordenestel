from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = 'apps.carga_archivos'

urlpatterns = [
    path('carga/', views.cargar_archivo_excel, name='cargar_archivo_excel'),
    path('listar/', views.listar_archivos_excel, name='listar_archivos_excel'),
    path('vista-previa/', views.vista_previa_archivo, name='vista_previa_archivo'),
 
    path('buscar-orden/', views.buscar_orden, name='buscar_orden'),
    path('eliminar/<int:archivo_id>/', views.eliminar_archivo, name='eliminar_archivo'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
