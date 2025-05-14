from django.contrib import admin
from django.urls import path, include
from theater_api_service.user.views import CreateUserView, ManageUserView

urlpatterns = [
    path("create/", CreateUserView.as_view(), name="user-create"),
    path("manage/", ManageUserView.as_view(), name="user-manage"),
]


app_name = "user"
