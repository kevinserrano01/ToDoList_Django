from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from myapp.models import Project, Tasks
# Fecha
from datetime import datetime
# Si no existe ese objeto devuelve la pagina 404
from django.shortcuts import get_object_or_404
# Importamos la clase del archivo forms para crear un formulario.
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def hello(request):
    """Funcion que crea una variable aqui y luego la muestra en un html"""
    title = 'TO DO LIST'
    username = "usuario"

    return render(request, 'myapp/index.html', {
        "titulo": title,
        "NombreUsuario": username
    })

# def projects(request):
#     """Mostrar los proyectos en formato JSON"""
#     projects = list(Project.objects.values())
#     return JsonResponse(projects, safe=False)

def projects(request):
    """Trae y muestra informacion de la base de datos"""
    # proyectos = list(Project.objects.values())
    proyectos = Project.objects.all()
    return render(request, 'myapp/proyectos.html', {
        "projects": proyectos
    })

# def tasks(request):
#     """Mostrar las tareas en formato JSON"""
#     tasks = list(Tasks.objects.values())
#     return JsonResponse(tasks, safe=False)

def tasks(request):
    """Mostrar las tareas por un id pero si no encuentra el obj le dice al cliente"""
    # task = Tasks.objects.get(title=title) # Buscar por nombre de tarea
    # task = get_object_or_404(Tasks, id=id)
    fecha_hora_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # Obtener la fecha y hora actual que se crea una tarea

    tasks = Tasks.objects.all()
    return render(request, 'myapp/tasks.html', {
        'tareas': tasks,
        'fechayHoraActual': fecha_hora_actual
    })

# def index(request):
#     """Funcion que crea una variable aqui y luego la muestra en un html"""
#     title = 'Titulo de la funcion index()!!'
#     username = "Kevin Serrano"

#     return render(request, 'myapp/index.html', {
#         "titulo": title,
#         "NombreUsuario": username
#     })

# TODO | CREAR NUEVA TAREA CON FORMULARIO POST ===================================>
def create_task(request):
    """Crea una nueva tarea generando un formulario en python"""
    if request.method == 'GET':
        return render(request, 'myapp/create_task.html', {
            'formulario': CreateNewTask()
        })
    else:
        tituloTarea = request.POST['title'] # Ver que me envia el formulario
        Tasks.objects.create(title=tituloTarea) # Creamos la tarea en la base de datos
        return redirect('tareas') # redirecciona a la url con el name='tareas' en urls.py
    
# TODO | ELIMINAR TAREA ================================================================>
def eliminar_tarea(request, tarea_id):
    tarea = Tasks.objects.get(id=tarea_id)
    tarea.delete()
    return redirect('tareas')


# TODO | MODIFICAR TAREA ================================================================>
def modificar_tarea(request, tarea_id):
    tarea = Tasks.objects.get(id=tarea_id)

    context = {
        'task': tarea
    }

    if request.POST:
        newtitle = request.POST['title']

        tarea.title = newtitle
        tarea.save()
    
    return render(request, 'myapp/modificar_tarea.html', context)



# TODO | CREAR NUEVO PROYECTO CON FORMULARIO POST ===================================>
def create_project(request):
    """Crea un nuevo proyecto generando un formulario en python"""
    if request.method == 'GET':
        return render(request, 'myapp/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        nameProject = request.POST['name'] # Ver que me envia el formulario
        Project.objects.create(name=nameProject) # Creamos la tarea en la base de datos
        return redirect('proyectos')

# TODO | ELIMINAR PROYECTO ================================================================>
def eliminar_proyecto(request, proyecto_id):
    proyecto = Project.objects.get(id=proyecto_id)
    proyecto.delete()
    return redirect('proyectos')