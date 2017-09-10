from django.test import TestCase


# Create your tests here.

class GreeterTest(TestCase):
    def test_not_found_on_empty(self):
        response = self.client.get('/greet/')
        self.assertEquals(response.status_code, 404)
