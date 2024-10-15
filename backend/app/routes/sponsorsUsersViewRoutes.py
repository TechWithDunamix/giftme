from ..controllers.supportersControllers.sponsorsUsersViewController import UserListController
from django.urls import path


sponsorUserListRoues = [
    path("users/all",UserListController.as_view())
]