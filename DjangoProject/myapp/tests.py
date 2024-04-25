from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from myapp.models import Users

class YourAppViewsTestCase(TestCase):
    def setUp(self):
        self.user = Users.objects.create(email='test@gmail.com', password='password', username='test_user')

    def test2(self):
        url = reverse('create_user')
        response = self.client.post(url, {'email': 'test@gmail.com', 'password': 'password', 'nickname': 'test_user2'})
        self.assertEqual(response.status_code, 201)

    def test3(self):
        url = reverse('update_user', args=[self.user.id])
        response = self.client.patch(url, {'nickname': 'updated_user'})
        self.assertEqual(response.status_code, 200)
