from ...common.customResponse import MakeResponse
from ...modules.authViews import APIView
from django.http import HttpRequest,HttpResponse
from ...models.sponsors import Sponsors
from rest_framework.permissions import AllowAny
from ...serializers.sponsorsSerializers import SponsorCreateSerializer
from rest_framework.serializers import Serializer
from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import timedelta,datetime
from django.db import models
import jwt
from config.settings import SECRET_KEY
class SponsorCreationController(APIView):
    permission_classes = [AllowAny]


    def post(self, request :HttpRequest, *args : list, **kwargs : dict) -> HttpResponse:

        serializer :Serializer = SponsorCreateSerializer(data = request.data)

        if not serializer.is_valid():
            return MakeResponse(serializer.errors, status=400)
        
        email :str = serializer.validated_data.get("email")
        sponsor :Sponsors  = Sponsors.get_or_create(email = email)
        print(sponsor.otp)


        return MakeResponse({"created" :True}, status=201)
    

class SponsorValidationOTPCntroller(APIView):
    permission_classes = [AllowAny]

    def post(self, request :HttpRequest, otp :int = None,*args :list, **kwargs):
        
        

        sponsor  = get_object_or_404(Sponsors, otp = otp)

        if sponsor.date_created + timedelta(minutes=90) < timezone.now():
            return MakeResponse({"error" : "OTP has expires"},
                                status=403,
                                message="OTP expired")
        

        token = jwt.encode({
            "user_emai" : sponsor.email,
            "user_id" : str(sponsor.id),
            "exp" : datetime.utcnow() + timedelta(minutes=90)
        },SECRET_KEY, algorithm="HS256")
        return MakeResponse({"success" : "soponsor",
                             "token" : token})


