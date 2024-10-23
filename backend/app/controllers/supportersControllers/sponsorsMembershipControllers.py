from ...models.userMembers import UserMembers
from ...models.authModels import AuthUserModel 
from ...modules.authManager import C_JWT_SponsorAuthentication
from rest_framework.views import APIView
from uuid import UUID
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from ...common.customResponse import MakeResponse
from rest_framework.permissions import IsAuthenticated
from ...models.userMemberships import UserMembership
class SponsorMembershipController(APIView):
    

    authentication_classes  :list = [C_JWT_SponsorAuthentication]
    
    permission_classes :list = [IsAuthenticated]
    
    def post(self,request :HttpRequest,user_id :UUID, *args : list , **kwargs : dict) -> HttpResponse:
        plan_id :UUID = request.GET.get("memberhip_plan_id", None)

        if not plan_id:
            return MakeResponse({"error" : "An error occured"}, 
                                message="Include 'memberhip_plan_id' in the request params ",
                                status=400)
        
        user :AuthUserModel = get_object_or_404(AuthUserModel, id = user_id)
        userplans = UserMembership.objects.filter(user = user).all()
        userplan = get_object_or_404(userplans, id = plan_id)
        


        return MakeResponse({"success" : "done"})


    
