from ..controllers import UserGalaryController
from django.urls import path

userGalaryRoutes = [
    path("user/gallery/create",UserGalaryController.as_view()),
    path("user/gallery/all",UserGalaryController.as_view()),
    path("user/gallery/<uuid:id>",UserGalaryController.as_view())


]