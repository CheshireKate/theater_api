from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import ForeignKey

from theater_api_service.theater.models import Ticket


class User(AbstractUser):
    tickets = ForeignKey(Ticket, on_delete=models.CASCADE)
