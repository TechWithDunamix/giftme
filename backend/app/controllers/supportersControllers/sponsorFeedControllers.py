from ...common.customResponse import MakeResponse 
from rest_framework.views import APIView 
from ...modules.authManager import C_JWT_SponsorAuthentication
from django.http import HttpRequest,HttpResponse
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from ...models.userPosts import UserPost,models
from django.utils import timezone
from ...serializers.sponsorsFeedSerializers import SponsorsPostFeedListSerializer
from rest_framework.serializers import Serializer
from django.shortcuts import get_object_or_404
class FeedsController(APIView):
    
    authentication_classes = [C_JWT_SponsorAuthentication]
    permission_classes = [AllowAny]


    def get(self , request :HttpRequest, id = None, *args : list, **kwargs : dict) -> HttpResponse:
        queries :list = [
                models.Q(draft = False) & models.Q(scheduled = False),
                models.Q(scheduled_for__lt = timezone.now())
            ]
        queryset = UserPost.objects.filter(*queries).select_related("user").prefetch_related("images")
        if not id:
            response = MakeResponse(
                request = request,
                paginate=True,
                serializer = SponsorsPostFeedListSerializer,
                queryset = queryset

                )
            
            return response

        obj :UserPost = get_object_or_404(queryset, id= id)
        serializer :Serializer =  SponsorsPostFeedListSerializer(obj,context = {
                                                        "request" : request
                                                        })
        return MakeResponse(
           serializer.data
        )