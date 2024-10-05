from .authRoutes import authUrls
from .userProfileRoutes import user_profile_routes
from .userProductRoutes import userProductListRoutes
from .userPostsRoutes import userPostRoutes
urlpatterns = [
    *authUrls,
    *user_profile_routes,
    *userProductListRoutes,
    *userPostRoutes
]
