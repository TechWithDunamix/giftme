from ..controllers.sponsorsControllers import SponsorCreationController
from django.urls import path
sponsorsRoutes = [
    path("sponsors/create",SponsorCreationController.as_view())
]