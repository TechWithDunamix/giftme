from ..controllers.userProfile import UserProfileController

from django.urls import path 


user_profile_routes = [
    path("user/profile",UserProfileController.as_view())
]