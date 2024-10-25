from django.urls import path
from ..controllers.supportersControllers.reactioncontrollers import ReactionController
reaction_routes = [
    path("reaction/new/<uuid:id>",ReactionController.as_view()),
    path("reaction/all/<uuid:id>",ReactionController.as_view())

]