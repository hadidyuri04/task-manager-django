from django.urls import path
from . import views

urlpatterns = [
    # This matches: http://127.0.0.1:8000/tasks/
    path('', views.task_list, name='task_list'),
    
    # This matches: http://127.0.0.1:8000/tasks/create/
    path('create/', views.task_create, name='task_create'),
    path('complete/<int:pk>/', views.task_complete, name='task_complete'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
]