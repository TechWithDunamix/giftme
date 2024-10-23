from django.urls import path
from ..controllers.supportersControllers.sponsorsMembershipControllers import SponsorMembershipController
sponsors_membership_routes = [
    path("membership/<uuid:user_id>",SponsorMembershipController.as_view())
]
