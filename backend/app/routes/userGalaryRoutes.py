from ..controllers.userGalaryController import UserGalaryController
from django.urls import path

userGalaryRoutes = [
    path("user/galary/create",UserGalaryController.as_view())
]