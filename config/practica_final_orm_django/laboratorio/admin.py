from django.contrib import admin
from .models import DirectorGeneral, Laboratorio,Producto

@admin.register(DirectorGeneral)
class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio')  # Muestra columnas en la lista
    list_filter = ('laboratorio',)  # Filtro por laboratorio
    search_fields = ('nombre', 'laboratorio__nombre')  # Búsqueda por nombre y laboratorio
    ordering = ('id',)  # Ordenar por ID
    list_per_page = 10  # Paginación

@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre', 'ciudad')
    ordering = ('id',)  # Ordenar por ID

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta')
    list_filter = ('laboratorio', 'f_fabricacion')  # Filtros por laboratorio y fecha
    search_fields = ('nombre', 'laboratorio__nombre')  # Búsqueda por nombre y laboratorio
    ordering = ('id',)  # Ordenar por ID
    list_editable = ('p_costo', 'p_venta')  # Permite editar precio en la lista
    list_per_page = 10  # Paginación