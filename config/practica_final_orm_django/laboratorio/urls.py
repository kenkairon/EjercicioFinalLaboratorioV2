from django.urls import path
from . import views

urlpatterns = [
    path('', views.laboratorio_list, name='laboratorio_list'),
    path('laboratorios/nuevo/', views.laboratorio_create, name='laboratorio_create'),
    path('laboratorios/<int:pk>/', views.laboratorio_detail, name='laboratorio_detail'),
    path('laboratorios/<int:pk>/editar/', views.laboratorio_update, name='laboratorio_update'),
    path('laboratorios/<int:pk>/eliminar/', views.laboratorio_delete, name='laboratorio_delete'),
]