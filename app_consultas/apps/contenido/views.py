from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import MediaForm
from .models import Media

def subir_media(request):
    if request.method == 'POST':
        form = MediaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Después de guardar los archivos con éxito, redirige a la página de visualización
            return redirect('ver_media')
    else:
        form = MediaForm()
    return render(request, 'contenido/subir_media.html', {'form': form})


def ver_media(request):
    # Obtener los archivos o videos subidos por el usuario
    media_items = Media.objects.all()
    
    # Agregar el objeto user al contexto
    context = {
        'media_items': media_items,
        'user': request.user  # Aquí se agrega el objeto user al contexto
    }
    return render(request, 'contenido/ver_media.html', context)


def eliminar_media(request, media_id):
    media = get_object_or_404(Media, id=media_id)
    if request.method == 'POST':
        media.delete()
        return HttpResponseRedirect(reverse('apps.contenido:ver_media'))
    return render(request, 'contenido/confirmar_eliminar.html', {'media': media})


@login_required
def mi_vista_protegida(request):
    # Tu lógica de vista aquí
    return render(request, 'contenido/ver_media.html')

