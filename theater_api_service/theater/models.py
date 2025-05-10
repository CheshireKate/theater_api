from django.contrib.auth.models import User
from django.db import models
from django.db.models import (
    TextField,
    ForeignKey,
    CharField,
    IntegerField,
    DateTimeField,
)
from django.core.exceptions import ValidationError
from django.utils import timezone


class Actor(models.Model):
    first_name = CharField(max_length=255, required=True)
    last_name = CharField(max_length=255, required=True)


class Genre(models.Model):
    name = CharField(primary_key=True)


class Play(models.Model):
    title = CharField(primary_key=True)
    description = TextField(max_length=300, blank=True, null=True)


class TheaterHall(models.Model):
    name = CharField(primary_key=True)
    rows = IntegerField()
    seats_in_row = IntegerField()


class Performance(models.Model):
    play = ForeignKey(Play, on_delete=models.CASCADE)
    theater_hall = ForeignKey(TheaterHall, on_delete=models.SET_NULL)
    show_time = DateTimeField()

    @staticmethod
    def validate_not_in_past(value):
        if value < timezone.now():
            raise ValidationError


class Reservation(models.Model):
    created_at = DateTimeField()
    user = User


class Ticket(models.Model):
    row = IntegerField()
    seat = IntegerField()
    performance = ForeignKey(Performance, on_delete=models.CASCADE)
    reservation = ForeignKey(Reservation, on_delete=models.CASCADE)

    @staticmethod
    def validate_row_and_seat(self):
        if (
            self.performance.theater_hall.rows < self.row
            or self.performance.theater_hall.seats_in_row < self.seat
        ):
            raise ValidationError
