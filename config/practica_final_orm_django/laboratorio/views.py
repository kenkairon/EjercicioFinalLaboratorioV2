from django.shortcuts import render, get_object_or_404, redirect
from .models import Laboratorio
from .forms import LaboratorioForm
from django.core.paginator import Paginator
from django.db.models import IntegerField
from django.db.models.functions import Cast, Substr

# 2. Listar laboratorio
def laboratorio_list(request):
    # Obtener el contador de visitas de las cookies del usuario
    visitas = int(request.COOKIES.get('visitas', 0)) + 1

    # Anotar el número extraído y ordenar por este valor
    laboratorios = Laboratorio.objects.annotate(
        numero=Cast(Substr('nombre', 12), IntegerField())
    ).order_by('numero')

    # Implementar paginación (10 elementos por página)
    paginator = Paginator(laboratorios, 5)
    page_number = request.GET.get('page')  # Obtener el número de página desde la URL
    page_obj = paginator.get_page(page_number)

    # Renderizar la página
    response = render(request, 'laboratorios/laboratorio_list.html', {
        'page_obj': page_obj,
        'visitas': visitas,
    })

    # Configurar la cookie de visitas
    response.set_cookie('visitas', visitas, max_age=60*60*24*30)  # 30 días de duración

    return response

# 2. Crear un nuevo laboratorio
def laboratorio_create(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('laboratorio_list')
    else:
        form = LaboratorioForm()
    return render(request, 'laboratorios/laboratorio_form.html', {'form': form})

# 3. Ver detalles de un laboratorio
def laboratorio_detail(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    return render(request, 'laboratorios/laboratorio_detail.html', {'laboratorio': laboratorio})

# 4. Actualizar un laboratorio
def laboratorio_update(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('laboratorio_list')
    else:
        form = LaboratorioForm(instance=laboratorio)
    return render(request, 'laboratorios/laboratorio_form.html', {'form': form})

# 5. Eliminar un laboratorio
def laboratorio_delete(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    if request.method == 'POST':
        laboratorio.delete()
        return redirect('laboratorio_list')
    return render(request, 'laboratorios/laboratorio_confirm_delete.html', {'laboratorio': laboratorio})

