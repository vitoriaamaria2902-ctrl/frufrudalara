from django.urls import path
from . import views

app_name = "frufrudalara"

urlpatterns = [
    path("", views.sobre , name="sobre"),
    path("login/", views.login, name="login"),
    path("produtos/", views.produtos, name="produtos"),
]