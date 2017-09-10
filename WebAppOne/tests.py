from django.test import TestCase


# Create your tests here.

class GreeterTest(TestCase):
    def test_not_found_on_empty(self):
        response = self.client.get('/greet/')
        self.assertEquals(response.status_code, 400)

    def test_not_found_on_wrong_gender(self):
        response = self.client.get('/greet/?gender=x')
        self.assertEquals(response.status_code, 400)

    def test_not_found_on_nil_last_name(self):
        response = self.client.get('/greet/?gender=f')
        self.assertEquals(response.status_code, 400)

    def test_not_found_on_empty_last_name(self):
        response = self.client.get('/greet/?gender=m&last_name=')
        self.assertEquals(response.status_code, 400)
