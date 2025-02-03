from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio

class LaboratorioTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Crear datos iniciales para pruebas
        cls.laboratorio = Laboratorio.objects.create(
            nombre='Laboratorio de Prueba',
            ciudad='Ciudad de Prueba',
            pais='País de Prueba'
        )

    # 1. Verificar datos en la base de datos simulada
    def test_modelo_laboratorio(self):
        lab = Laboratorio.objects.get(id=self.laboratorio.id)
        self.assertEqual(lab.nombre, 'Laboratorio de Prueba')
        self.assertEqual(lab.ciudad, 'Ciudad de Prueba')
        self.assertEqual(lab.pais, 'País de Prueba')

    # 2. Verificar respuesta HTTP 200 para URL de detalle
    def test_url_detalle_status_code(self):
        response = self.client.get(f'/laboratorios/{self.laboratorio.pk}/')
        self.assertEqual(response.status_code, 200)

    # 3. Verificar vista usando reverse, template y contenido
    def test_vista_detalle(self):
        response = self.client.get(reverse('laboratorios', args=[self.laboratorio.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laboratorio/laboratorio_detail.html')
        self.assertContains(response, self.laboratorio.nombre)
