from django.urls import path
from ..controllers import PostFeedController 


sponsors_feeds_routes = [
    path("feeds/posts",PostFeedController.as_view()),
    path("feeds/pasts/<uuid:id>",PostFeedController.as_view())

]