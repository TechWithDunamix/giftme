from .authRoutes import authUrls
from .userProfileRoutes import user_profile_routes

urlpatterns = [
    *authUrls,
    *user_profile_routes
]
