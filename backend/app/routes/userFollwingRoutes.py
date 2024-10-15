from ..controllers.supportersControllers.userFollowingController import SponsorFollowingUserController

from django.urls import path


user_following_routes = [
    path("user/followership/<uuid:user_id>",SponsorFollowingUserController.as_view())
]