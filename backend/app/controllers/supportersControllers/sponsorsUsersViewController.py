from ...models.authModels import AuthUserModel 
from django.http import HttpRequest,HttpResponse 
from rest_framework.views import APIView
from ...common.customResponse import MakeResponse 
from rest_framework.permissions import AllowAny
from ...modules.authManager import C_JWT_SponsorAuthentication, C_JWT_UserAuthentication
from ...serializers.usersViewSerializers import UserListViewSerializer,UserDetailViewSerializer
from django.shortcuts import get_list_or_404
from rest_framework.serializers import Serializer
class UserListController(APIView):
    permission_classes = [AllowAny]
    authentication_classes = [C_JWT_SponsorAuthentication, C_JWT_UserAuthentication]

    def get(self, request :HttpRequest, id = None, *args : list, **kwargs :dict) -> HttpResponse:
        if not id:

            query_set :AuthUserModel  = AuthUserModel.objects.all().prefetch_related("user_profile")
        
            return MakeResponse(
                paginate=True,
                queryset = query_set,
                serializer = UserListViewSerializer,
                request = request
            )
        
        obj :AuthUserModel = get_list_or_404(AuthUserModel, id = id)
        serializer :Serializer = UserDetailViewSerializer(obj,context = {
            "request" : request
        },many = True)
        return MakeResponse(serializer.data)