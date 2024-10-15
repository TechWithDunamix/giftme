from django.http import HttpRequest,HttpResponse
from django.shortcuts import get_object_or_404
from ...models.authModels import AuthUserModel
from ...models.sponsors import Sponsors
from ...models.userFollowerShip import Followership
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from ...modules.authManager import C_JWT_SponsorAuthentication
from ...common.customResponse import MakeResponse

class SponsorFollowingUserController(APIView):
    authentication_classes = [C_JWT_SponsorAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request :HttpRequest, user_id = None, *args: list, **kwargs : dict):

        user = get_object_or_404(AuthUserModel, id = user_id)

        sponsor, created = Sponsors.objects.get_or_create(email = request.user.email)
        if Followership.objects.filter(user = user,sponsor = sponsor).exists():
            return MakeResponse({"success" : "Follwed"})

        Followership.objects.create(user = user,sponsor = sponsor)
        
        return MakeResponse({"success" : "Followed"})

    def delete(self, request :HttpRequest, user_id = None, *args :list , **kwargs :dict):
         user = get_object_or_404(AuthUserModel, id = user_id)

         sponsor, created = Sponsors.objects.get_or_create(email = request.user.email)
         obj = get_object_or_404(Followership, user = user, sponsor = sponsor)
         print(obj)
         obj.delete()
         return MakeResponse({"success" : "Unfollowed"})
