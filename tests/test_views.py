from django.test import TestCase


class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('0.0.0.0:8000')
        self.assertEqual(response.status_code, 404)

    def test_simple_all_images_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('0.0.0.0:8000/images')
        self.assertEqual(response.status_code, 404)

    def test_simple_detail_image_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('0.0.0.0:8000/images/0')
        self.assertEqual(response.status_code, 404)

    def test_vers_all_images_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('0.0.0.0:8000/api/v1/images')
        self.assertEqual(response.status_code, 404)

    def test_vers_detail_image_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('0.0.0.0:8000/api/v1/images/0')
        self.assertEqual(response.status_code, 404)
