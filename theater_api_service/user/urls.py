from django.contrib import admin
from django.urls import path, include
from theater_api_service.user.views import CreateUserView, ManageUserView

urlpatterns = [
    path("create/", CreateUserView.as_view(), "user-create"),
    path("manage/", ManageUserView.as_view(), "user-manage"),
    path("admin/", admin.site.urls),
    path("api/theater", include("theater_api_service.theater.urls")),
]


app_name = "user_urls"
