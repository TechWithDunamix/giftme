from .authRoutes import authUrls
from .userProfileRoutes import user_profile_routes
from .userProductRoutes import userProductListRoutes
from .userPostsRoutes import userPostRoutes
from .userGalaryRoutes import userGalaryRoutes
from .userMembershipPlansRoutes import usermembershipsroutes
from .sponsoraAuthRoutes import sponsorsRoutes
from .sponsorFeedsRoutes import sponsors_feeds_routes
from .sponsorsUsersViewRoutes import sponsorUserListRoues
from .userFollwingRoutes  import user_following_routes
urlpatterns = [
    *authUrls,
    *user_profile_routes,
    *userProductListRoutes,
    *userPostRoutes,
    *userGalaryRoutes,
    *usermembershipsroutes,
    *sponsorsRoutes,
    *sponsors_feeds_routes,
    *sponsorUserListRoues,
    *user_following_routes
]
