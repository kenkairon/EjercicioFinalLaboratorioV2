from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

class Laboratorio(models.Model):
    nombre = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255, null=True, blank=True)  # Valor por defecto
    pais = models.CharField(max_length=255, null=True, blank=True)   # Valor por defecto

    def __str__(self):
        return self.nombre


class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=255, null=True, blank=True, default="General")  # Valor por defecto

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    f_fabricacion = models.DateField(null=True, blank=True, default=date(2023, 1, 1))  # Fecha por defecto
    p_costo = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)  # Valor por defecto
    p_venta = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)  # Valor por defecto

    def clean(self):
        if self.f_fabricacion:
            if self.f_fabricacion < date(2015, 1, 1):
                raise ValidationError("La fecha de fabricación no puede ser anterior a 2015.")

    def __str__(self):
        return self.nombre
