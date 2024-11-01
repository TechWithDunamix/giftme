from django.urls import path
from ..controllers import PostFeedController ,ProductsFeeds


sponsors_feeds_routes = [
    path("feeds/posts",PostFeedController.as_view()),
    path("feeds/posts/<uuid:id>",PostFeedController.as_view()),
    path("feeds/products",ProductsFeeds.as_view()),
    path("feeds/products/<uuid:id>",ProductsFeeds.as_view()),



]