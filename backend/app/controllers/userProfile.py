import json
from ..common.customResponse import MakeResponse
from ..modules.authViews import C_APIView,APIView
from rest_framework.authentication import TokenAuthentication
from django.http import HttpRequest,HttpResponse
from ..serializers.userProfileSerializer import UserProfileCreationSerializer,UserProfileViewSerializer
from rest_framework.serializers import Serializer
from ..models.userProfile import UserProfile
from django.db import transaction
class UserProfileController(C_APIView):
    protected = False


    def get(self,request: HttpRequest,*args:list , **kwargs: dict) -> HttpRequest:
        obj:UserProfile =  UserProfile.objects.get(user = request.user)
        context:dict = {
            "request":request
        }
        serializer:Serializer = UserProfileViewSerializer(obj,context = context)
        return MakeResponse(data = serializer.data)

    @transaction.atomic
    def post(self,request:HttpRequest,*args:list,**kwargs: dict) -> HttpResponse:

        if UserProfile.objects.filter(user = request.user):
            return MakeResponse({"error":"User already have an account"},status=400)
        serializer:Serializer = UserProfileCreationSerializer(data = request.data)
        if not serializer.is_valid():
            return MakeResponse(data=serializer.errors,status=400,message="Bad request")

        userData:dict = {
            "user" : request.user,
            "bio" : serializer.data.get('bio'),
            "interests" : serializer.data.get('interest'),
            "profile_image" : request.FILES.get('profile_image'),
            "cover_image" : request.FILES.get('cover_image'),
            "socials" : serializer.data.get('socials')
        }

        UserProfile.objects.create(**userData)
        return MakeResponse(data = serializer.data,status=200)