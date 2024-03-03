from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .forms import ArchivoExcelForm
from .models import ArchivoExcel
import pandas as pd

from django.shortcuts import render
from .forms import ArchivoExcelForm

def cargar_archivo_excel(request):#carga el archivo
    if request.method == 'POST':
        form = ArchivoExcelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            mensaje = 'El archivo se cargó satisfactoriamente.'
            # Después de guardar el archivo y establecer el mensaje, limpiamos el formulario
            form = ArchivoExcelForm()
        else:
            mensaje = 'Hubo un error al procesar el formulario. Por favor, inténtelo de nuevo.'
    else:
        form = ArchivoExcelForm()
        mensaje = None

    return render(request, 'carga_archivos/cargar_archivo_excel.html', {'form': form, 'mensaje': mensaje})


def listar_archivos_excel(request):#muestra los archivos cargados
    archivos = ArchivoExcel.objects.all()
    return render(request, 'carga_archivos/listar_archivos_excel.html', {'archivos': archivos})



def eliminar_archivo(request, archivo_id):#da la posibilidad de eliminar archivos
    archivo = get_object_or_404(ArchivoExcel, pk=archivo_id)

    if request.method == 'POST':
        archivo.delete()
        return redirect('apps.carga_archivos:listar_archivos_excel')

    return render(request, 'carga_archivos/confirmar_eliminar_archivo.html', {'archivo': archivo})


def vista_previa_archivo(request):#muestra el ultimo archivo cargado
    if request.method == 'GET' and 'numero_orden' in request.GET:
        numero_orden = request.GET['numero_orden']
        archivo = ArchivoExcel.objects.filter(numero_de_orden=numero_orden).last()
    else:
        archivo = ArchivoExcel.objects.last()

    if archivo:
        archivo_path = archivo.archivo.path
        try:
            df = pd.read_excel(archivo_path)
            tabla_html = df.to_html()
            return render(request, 'carga_archivos/vista_previa_archivo.html', {'tabla_html': tabla_html})
        except Exception as e:
            mensaje_error = f"No se pudo cargar el archivo: {str(e)}"
            return render(request, 'carga_archivos/error_vista_previa.html', {'mensaje_error': mensaje_error})
    else:
        mensaje = "No hay archivos cargados."
        return render(request, 'carga_archivos/vista_previa_archivo.html', {'mensaje': mensaje})

# En tu vista para procesar y mostrar el archivo Excel


def buscar_orden(request):
    mensaje = "Ingrese Numero de orden.\nSu nombre o fecha de cita o instalación"
    resultados = None

    if request.method == 'GET' and 'q' in request.GET:
        termino_busqueda = request.GET['q']
        archivo = ArchivoExcel.objects.last()  # Obtener el último archivo cargado
        if archivo:
            archivo_path = archivo.archivo.path
            try:
                df = pd.read_excel(archivo_path)
                # Realizar la búsqueda dentro del DataFrame
                columnas = df.columns  # Obtener nombres de columnas
                resultados = []

                # Recorrer todas las filas y columnas para buscar el término de búsqueda
                for index, row in df.iterrows():
                    for col in columnas:
                        if str(termino_busqueda).lower() in str(row[col]).lower():
                            resultados.append(row.to_dict())  # Convertir la fila a un diccionario
                            break  # Salir del bucle interior si se encuentra una coincidencia

            except Exception as e:
                mensaje = f"No se pudo leer el archivo: {str(e)}"
    else:
        mensaje = "No hemos podido localizar lo solicittado.\nEvite espacios.\nSi el problema persiste contactenos"

    return render(request, 'carga_archivos/buscar_orden.html', {'resultados': resultados, 'mensaje': mensaje})


