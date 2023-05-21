from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.loginPage, name="login"),
    path("register", views.registerPage, name="register"),
    path("logout", views.logoutUser, name="logout"),
    path("training", views.trainModel, name="training"),
    path('lungcancer/upload/<str:filename>', views.serve_photo),
]