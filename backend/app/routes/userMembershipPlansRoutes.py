from django.urls import path
from ..controllers import UserMembershipPlanController
usermembershipsroutes = [
    path("user/memberships/create",UserMembershipPlanController.as_view()),
    path("user/memberships/all",UserMembershipPlanController.as_view()),
    path("user/memberships/<uuid:id>",UserMembershipPlanController.as_view())




]