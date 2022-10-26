from django.test import TestCase
from elements.models import ImageData


class ModelsTestCase(TestCase):
    def test_image_save(self):
        """Image can be saved"""
        image = ImageData.objects.create(title="Test tilte")
        image.description = "Test description"
        image.image = "www.image.com/image.jpg"
        image.save()
        self.assertIsNone(image.id)
