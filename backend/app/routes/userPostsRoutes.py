from ..controllers import UserPostController 
from django.urls import path
userPostRoutes = [
path("user/posts/create",UserPostController.as_view()),
path("user/posts/all",UserPostController.as_view()),
path("user/posts/<uuid:id>",UserPostController.as_view())

]