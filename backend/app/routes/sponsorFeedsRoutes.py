from django.urls import path
from ..controllers import SponsorFeedController 


sponsors_feeds_routes = [
    path("sponsors/feeds",SponsorFeedController.as_view())
]