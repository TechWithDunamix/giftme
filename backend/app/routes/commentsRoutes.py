from django.urls import path
from ..controllers.supportersControllers.commentControllers import CommentController
comment_routes = [
    path("comment/new/<uuid:id>",CommentController.as_view()),
    path("comment/all/<uuid:id>",CommentController.as_view()),

]