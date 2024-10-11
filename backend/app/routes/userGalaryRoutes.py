from ..controllers import UserGalaryController
from django.urls import path

userGalaryRoutes = [
    path("user/galary/create",UserGalaryController.as_view()),
    path("user/galary/all",UserGalaryController.as_view()),
    path("user/galary/<uuid:id>",UserGalaryController.as_view())


]