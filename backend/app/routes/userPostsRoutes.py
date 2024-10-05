from ..controllers.userPostController import UserPostController 
from django.urls import path
userPostRoutes = [
path("user/posts/create",UserPostController.as_view())
]