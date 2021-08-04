import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .views import PostNew


class PostNewTests(TestCase):

    def test_run_server(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)