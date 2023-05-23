from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='home'),
    path('projects/', views.projects, name='proyectos'),
    path('tasks/', views.tasks, name='tareas'),
    path('createTask/', views.create_task, name='crear_tarea'),
    path('eliminarTarea/<int:tarea_id>', views.eliminar_tarea, name='eliminar_tarea'),
    path('modificarTarea/<int:tarea_id>', views.modificar_tarea, name='modificar_tarea'),
    path('createProject/', views.create_project, name='crear_proyecto'),
    path('eliminarProyecto/<int:proyecto_id>', views.eliminar_proyecto, name='eliminar_proyecto')
]