import json
from ..common.customResponse import MakeResponse
from ..modules.authViews import C_APIView,APIView
from rest_framework.authentication import TokenAuthentication
from django.http import HttpRequest,HttpResponse
from ..serializers.userProfileSerializer import (UserProfileCreationSerializer,
                                                 UserProfileViewSerializer,
                                                 UserProfileUpdateSerializer)
from rest_framework.serializers import Serializer
from ..models.userProfile import UserProfile
from ..models.authModels import AuthUserModel
from django.db import transaction
class UserProfileController(C_APIView):
    protected = False


    def get(self,request: HttpRequest,*args:list , **kwargs: dict) -> HttpRequest:
        if not UserProfile.objects.filter(user = request.user).exists():
            return MakeResponse(
                {"error":"User has no profile yet !"},
                status=400,
                message="User has no Profile")
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
            "bio" : serializer.validated_data.get('bio'),
            "interests" : serializer.validated_data.get('interests'),
            "profile_image" : request.FILES.get('profile_image'),
            "cover_image" : request.FILES.get('cover_image'),
            "socials" : serializer.validated_data.get('socials')
        }

        

        UserProfile.objects.create(**userData)
        return MakeResponse(data = serializer.data,status=200)
    
    @transaction.atomic
    def put(self,request :HttpRequest,*args: list, **kwargs: dict) -> HttpResponse:

        serializer:Serializer = UserProfileUpdateSerializer(data = request.data)

        if not serializer.is_valid():
            return MakeResponse(data=serializer.errors,status=400)
        

        userData:dict = {
            "username" : serializer.validated_data.get("username",request.user.username),
            "email" : serializer.validated_data.get("email",request.user.email),
            "first_name" : serializer.validated_data.get("email",request.user.first_name),
            "last_name" : serializer.validated_data.get("email",request.user.last_name),
            "country" : serializer.validated_data.get("country",request.user.country)

            }
        
        userProfileData:dict = {
            "bio" : serializer.validated_data.get("bio",request.user.user_profile.bio),
            "interests" : serializer.validated_data.get("interests",request.user.user_profile.interests),
            "profile_image" : request.FILES.get("profile_image",request.user.user_profile.profile_image),
            "cover_image" : request.FILES.get("cover_image",request.user.user_profile.cover_image),
            "socials" : serializer.validated_data.get("socials",request.user.user_profile.interests),
            "paymentDetails" : serializer.validated_data.get("paymentDetails",request.user.user_profile.paymentDetails),

        }

        for key,value in userData.items():
            setattr(request.user,key,value)

        request.user.save()

        for key,value in userProfileData.items():
            setattr(request.user.user_profile,key,value)

        request.user.user_profile.save()


        return MakeResponse({"update":True})