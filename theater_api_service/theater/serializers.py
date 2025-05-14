from theater_api_service.user.models import User

from rest_framework import serializers

from theater_api_service.theater.models import Play, Actor, Genre, TheaterHall, Performance
from theater_api_service.theater.models import Reservation, Ticket


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ["first_name", "last_name"]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["name"]


class PlaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Play
        fields = ["title", "description"]


class TheaterHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheaterHall
        fields = ["name", "rows", "seats_in_row"]


class PerformanceSerializer(serializers.ModelSerializer):
    play = serializers.SlugRelatedField(queryset=Play.objects.all(), many=False, slug_field="title")
    theater_hall = serializers.SlugRelatedField(queryset=TheaterHall.objects.all(), many=False, slug_field="name")

    class Meta:
        model = Performance
        fields = ["play", "theater_hall", "show_time"]


class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Reservation
        fields = ["created_at", "user"]


class TicketSerializer(serializers.ModelSerializer):
    performance = serializers.SlugRelatedField(queryset=Performance.objects.all(), many=False, slug_field="play__title")
    reservation = serializers.SlugRelatedField(queryset=Reservation.objects.all(), many=False, slug_field="created_at")

    class Meta:
        model = Ticket
        fields = ["row", "seat", "performance", "reservation"]
