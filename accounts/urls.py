""" urls for accounts app """

from django.urls import path
from accounts import views

urlpatterns = [
    path("signup/", views.register_user, name="register_user"),
]
