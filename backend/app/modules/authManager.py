import jwt
from django.http import HttpRequest
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from config.settings import SECRET_KEY
from ..models.authModels import AuthUserModel
from ..models.sponsors import Sponsors
from typing import Tuple
class C_JWT_UserAuthentication(BaseAuthentication):

    def authenticate(self, request :HttpRequest):
        header :str = request.headers.get("Authorization", None)

        if not header:
            return None 
        
        try:
            prefix , token = header.split(" ")

            if prefix.lower() != "bearer":
                raise AuthenticationFailed("Invalid Token Prefix")

        except ValueError:
            raise AuthenticationFailed("Invalid header format")
        
        return self.authenticate_token(token)
        
    def authenticate_token(self, token :str) -> Tuple[AuthUserModel | None]:
        try :
            payload :dict = jwt.decode(token, SECRET_KEY,algorithms=["HS256"])
        
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token expired")
        
        except jwt.InvalidTokenError:
            raise AuthenticationFailed("Invalid Token")
        
        try:
            user = AuthUserModel.objects.get(id = payload['user_id'])

        except AuthUserModel.DoesNotExist:
            raise AuthenticationFailed("User Not FOund")
        
        return (user, None)
            




        
class C_JWT_SponsorAuthentication(BaseAuthentication):

    def authenticate(self, request :HttpRequest):
        header :str = request.headers.get("Authorization", None)

        if not header:
            return None 
        
        try:
            prefix , token = header.split(" ")

            if prefix.lower() != "bearer":
                raise AuthenticationFailed("Invalid Token Prefix")

        except ValueError:
            raise AuthenticationFailed("Invalid header format")
        
        return self.authenticate_token(token)
        
    def authenticate_token(self, token :str) -> Tuple[AuthUserModel | None]:
        try :
            payload :dict = jwt.decode(token, SECRET_KEY,algorithms=["HS256"])
        
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token expired")
        
        except jwt.InvalidTokenError:
            raise AuthenticationFailed("Invalid Token")
        
        try:
            user = Sponsors.objects.get(id = payload['user_id'])

        except Sponsors.DoesNotExist:
            raise AuthenticationFailed("User Not FOund")
        
        return (user, None)
            




        
