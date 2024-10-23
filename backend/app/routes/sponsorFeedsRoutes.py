from django.urls import path
from ..controllers import FeedsController 


sponsors_feeds_routes = [
    path("feeds",FeedsController.as_view()),
    path("feeds/<uuid:id>",FeedsController.as_view())

]