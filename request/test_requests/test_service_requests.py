from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status

class TestViews(APITestCase):

    def setUp(self):
        self.create_url = reverse('create_requests')
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')
        self.reset_data = {
            "title": "clean pond",
            "description": "clean the entire pond",
            "status": "pending",
            "priority": "high",
            "client": 2,
            "staff": [
                1,
                2,
                3
            ]
        }
        super().setUp()
    
    def tearDown(self):
        super().tearDown()
    
    def test_create_request_authentication(self):
        response = self.client.post(self.create_url, self.reset_data, format='json')
        self.assertEqual(response, status.HTTP_401_UNAUTHORIZED)