
from django.contrib.auth.models import User
from django.test import TestCase


class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'password'}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        # send login data
        response = self.client.post('/signup/', self.credentials, follow=True)
        # should be logged in now
        self.assertFalse(response.context['user'].is_active)
