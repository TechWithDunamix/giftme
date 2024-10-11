from ...common.customResponse import MakeResponse 
from rest_framework.views import APIView 
from ...modules.authManager import C_JWT_SponsorAuthentication
from django.http import HttpRequest,HttpResponse
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from ...models.userPosts import UserPost,models
from django.utils import timezone


class SponsorFeedController(APIView):
    
    authentication_classes = [C_JWT_SponsorAuthentication]
    permission_classes = [AllowAny]


    def get(self , request :HttpRequest, id = None, *args : list, **kwargs : dict) -> HttpResponse:
        if not id:
            queries :list = [
                models.Q(draft = False) & models.Q(scheduled = False),
                models.Q(scheduled_for__lt = timezone.now())
            ]
            queryset = UserPost.objects.filter(*queries)
            
        return MakeResponse({"success" : True})