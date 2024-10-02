import json
from ..common.customResponse import MakeResponse
from ..modules.authViews import C_APIView,APIView
from rest_framework.authentication import TokenAuthentication
from django.http import HttpRequest,HttpResponse
from ..serializers.userProfileSerializer import UserProfileCreationSerializer
from rest_framework.serializers import Serializer
class UserProfile(C_APIView):
    protected = False
    def post(self,request:HttpRequest,*args:list,**kwargs: dict) -> HttpResponse:
        serializer:Serializer = UserProfileCreationSerializer(data = request.data)
        if not serializer.is_valid():
            return MakeResponse(data=serializer.errors,status=400,message="Bad request")

        # print(json.loads(serializer.data.get("interest")[0]))
        return MakeResponse(data = serializer.data,status=200)