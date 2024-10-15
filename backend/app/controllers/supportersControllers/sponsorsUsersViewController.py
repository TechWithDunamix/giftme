from ...models.authModels import AuthUserModel 
from django.http import HttpRequest,HttpResponse 
from rest_framework.views import APIView
from ...common.customResponse import MakeResponse 
from rest_framework.permissions import AllowAny
from ...serializers.usersViewSerializers import UserListViewSerializer

class UserListController(APIView):
    permission_classes = [AllowAny]

    def get(self, request :HttpRequest, id = None, *args : list, **kwargs :dict) -> HttpResponse:
        query_set :AuthUserModel  = AuthUserModel.objects.all().prefetch_related("user_profile")
        
        return MakeResponse(
            paginate=True,
            queryset = query_set,
            serializer = UserListViewSerializer,
            request = request
        )