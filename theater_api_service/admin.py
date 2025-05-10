from django.contrib import admin

from theater_api_service.theater.models import (
    Actor,
    Genre,
    Play,
    TheaterHall,
    Performance,
    Reservation,
    Ticket,
)

admin.site.register(Play)
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(TheaterHall)
admin.site.register(Performance)
admin.site.register(Reservation)
admin.site.register(Ticket)

admin.register()
