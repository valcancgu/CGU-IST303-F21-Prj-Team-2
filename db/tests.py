import pytest
import uuid
from django.test import TestCase

from django.contrib.auth.models import User



@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('praveen', 'praveen@gmail.com', 'prpassword')
    assert User.objects.count() == 1


@pytest.fixture
def test_password():
    return 'strong-test-pass'


class _DatabaseFailure:
    def __init__(self, wrapped, message):
        self.wrapped = wrapped
        self.message = message

    def __call__(self):
        raise AssertionError(self.message)
from django.test import TestCase

# Create your tests here.
