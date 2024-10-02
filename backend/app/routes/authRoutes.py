from ..controllers.auth import UserSignin ,UserLogin
from django.urls import include,path
authUrls = [
    path("auth/signup",UserSignin.as_view()),
    path("auth/login",UserLogin.as_view())

]