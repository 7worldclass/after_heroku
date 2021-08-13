from django.http import response
from django.test import SimpleTestCase

class My_app(SimpleTestCase):
    def test_home_exist(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_home_exist(self):
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)
    def test_about_exist(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
