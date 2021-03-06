from django.test import TestCase


class HomeTest(TestCase):
    def test_get(self):
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)

    def test_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'homepage/index.html')
