from unittest import TestCase

from django.contrib.auth import get_user_model
from rest_framework.authtoken.admin import User
from rest_framework.test import APIClient
from rest_framework import status

from django.urls import reverse

from theater_api_service.theater.models import Play

ADMIN_URL = reverse("admin/")
PLAYS_URL = reverse("theater:play-list")

def user_detail_url(user_id):
    return reverse("users:user-detail", kwargs={"id": user_id})

def play_detail_url(play_id):
    return reverse("theater:play-detail", kwargs={"id": play_id})


class UnauthenticatedTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        res = self.client.get(ADMIN_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_play_user(self):
        play = Play.objects.create(title="A", description="B")
        res = self.client.delete(play)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class ListRetrieveTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "test@test.com",
            "testpass",
        )
        self.client.force_authenticate(self.user)

    def test_list(self):
        res = self.client.get(PLAYS_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_retrieve(self):
        play = Play.objects.create(title="A", description="B")
        result_url = play_detail_url(play.id)
        res = self.user.get(result_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)


class AdminManageTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin_user = User.objects.create_superuser(
            email="admin@example.com",
            password="adminpass"
        )
        self.client.force_authenticate(self.admin_user)


    def admin_delete(self):
        play = Play.objects.create(title="A", description="B")
        self.admin_user.delete(play)
        result_url = play_detail_url(play.id)
        self.assertEqual(result_url.status_code, status.HTTP_400_BAD_REQUEST)


    def admin_retrieve_user(self):
        user = get_user_model().objects.create_user(
            "test@test.com",
            "testpass",
        )
        user_url = user_detail_url(user.id)
        res = self.admin_user.get(user_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
