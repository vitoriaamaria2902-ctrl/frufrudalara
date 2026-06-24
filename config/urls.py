from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("frufrudalara/", include("frufrudalara.urls")),
    path("admin/", admin.site.urls),
]
