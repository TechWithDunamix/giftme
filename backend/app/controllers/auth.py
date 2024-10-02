from rest_framework.serializers import Serializer
from django.db import transaction
from django.http import HttpRequest,HttpResponse
from rest_framework.views import APIView 
from asgiref.sync import sync_to_async
from asgiref.sync import async_to_sync
from ..serializers.authSerializers import  UserSignupSerializer,UserLoginSerializer
from ..common.customResponse import MakeResponse
from ..models.authModels import AuthUserModel
from ..common.authUtils import AuthenticationCheck 
from ..common import authUtils
from ..modules.authViews import C_APIView
from rest_framework.authtoken.models import Token
auth: AuthenticationCheck = AuthenticationCheck()
class UserSignin(APIView):
    def create_user(self,**data):
        return AuthUserModel.objects.create_user(**data)
    
    @transaction.atomic
    def  post(self,request:HttpRequest,*args: list,**kwargs: dict) -> HttpResponse:
        serializer:Serializer = UserSignupSerializer(data = request.data)
        
        if not serializer.is_valid():
            return MakeResponse(serializer.errors,status=400)
        
        user = self.create_user(**serializer.data)
        
        return  MakeResponse(request.data,message="User registered success !")
        




class UserLogin(APIView):

    def post(self,request:HttpRequest,*args,**kwarhs) -> HttpResponse:
        serializer:Serializer = UserLoginSerializer(data = request.data)
    
        if not serializer.is_valid():
            return MakeResponse(serializer.errors,status=400)
        
        user = auth.authenticate(
            email=serializer.data.get("email",None),
            password=serializer.data.get("password",None)

        )

        if not user:
            errors:dict = {
                "auth":"Invalid user credentials"
            }
            return MakeResponse(errors,status=400)

        # token:str = authUtils.make_token(user.id)
        token:Token = Token.objects.get_or_create(user = user)[0]
        print(token)
        return MakeResponse({
            "auth" : "Login success",
            "token":token.key
        },status=200)

        

