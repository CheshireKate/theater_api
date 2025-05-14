"""
URL configuration for theater_api_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from theater_api_service.theater.views import (
    ActorViewSet,
    GenreViewSet,
    PlayViewSet,
    TheaterHallViewSet,
    PerformanceViewSet,
    TicketViewSet,
    ReservationViewSet,
)

router = routers.DefaultRouter()


router.register("actors", ActorViewSet, basename="actor")
router.register("genres", GenreViewSet, basename="genre")
router.register("plays", PlayViewSet, basename="play")
router.register("theater_halls", TheaterHallViewSet, basename="theater_hall")
router.register("performances", PerformanceViewSet, basename="performance")
router.register("tickets", TicketViewSet, basename="ticket")
router.register("reservations", ReservationViewSet, basename="reservation")

urlpatterns = [
    path("", include(router.urls)),
]


app_name = "theater_api_service.theater"
