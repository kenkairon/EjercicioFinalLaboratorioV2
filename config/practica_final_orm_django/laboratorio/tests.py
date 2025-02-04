from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio

class LaboratorioTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Crear un laboratorio de prueba en la base de datos
        cls.laboratorio = Laboratorio.objects.create(nombre="Laboratorio 001")

    def test_laboratorio_data(self):
        """Verifica que los datos creados en setUpTestData coincidan en la BD."""
        laboratorio = Laboratorio.objects.get(id=self.laboratorio.id)
        self.assertEqual(laboratorio.nombre, "Laboratorio 001")

    def test_laboratorio_list_url(self):
        """Verifica que la URL de listar laboratorios devuelve HTTP 200."""
        response = self.client.get(reverse('laboratorio_list'))
        self.assertEqual(response.status_code, 200)

    def test_laboratorio_detail_url(self):
        """Verifica que la URL de detalle de laboratorio devuelve HTTP 200."""
        response = self.client.get(reverse('laboratorio_detail', args=[self.laboratorio.id]))
        self.assertEqual(response.status_code, 200)

    def test_laboratorio_list_template(self):
        """Verifica que se use la plantilla correcta y el contenido esperado en la lista de laboratorios."""
        response = self.client.get(reverse('laboratorio_list'))
        self.assertTemplateUsed(response, 'laboratorios/laboratorio_list.html')
        self.assertContains(response, "Laboratorio 001")