from ..controllers import SponsorCreationController,SponsorValidationOTPCntroller
from django.urls import path
sponsorsRoutes = [
    path("sponsor/create",SponsorCreationController.as_view()),
    path("sponsor/validate/<int:otp>",SponsorValidationOTPCntroller.as_view())
]