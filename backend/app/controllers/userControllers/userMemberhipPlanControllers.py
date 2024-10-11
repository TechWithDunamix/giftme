from ...common.customResponse import MakeResponse
from ...modules.authViews import C_APIView
from django.http import HttpRequest,HttpResponse
from ...serializers.userMembershipsSerializers import UserMembershipCreateSerializer,UserMembershipsViewSerializer,UserMembershipUpdateSerializer
from ...models.userMemberships import UserMembership
from rest_framework.serializers import Serializer
from django.shortcuts import get_object_or_404
class UserMembershipPlanController(C_APIView):
    def get(self, request :HttpRequest, id = None, *args : list, **kwargs:dict) -> HttpResponse:
        queryset :UserMembership = UserMembership.objects.filter(user = request.user).all()

        if not id:                                          
            
            
            serializer :Serializer = UserMembershipsViewSerializer(queryset,many = True,context = {
                "request" : request
            })
            return MakeResponse(serializer.data)

        obj :UserMembership = get_object_or_404(queryset,id = id)

        serializer :Serializer = UserMembershipsViewSerializer(obj,context = {
            "request" : request
        })
        return MakeResponse(serializer.data)



    def post(self, request :HttpRequest, *args :list , **kwargs : dict) ->  HttpResponse:
        if UserMembership.objects.filter(user = request.user).__len__() == 4:
            return MakeResponse({"error" : "You can not have more than one membership plan"},status=400)

        serializer :Serializer = UserMembershipCreateSerializer(data = request.data,context = {
            "request" : request
        })

        if not serializer.is_valid():
            return MakeResponse(serializer.errors,status=400)
        
        postData :dict = {}
        for key,val in serializer.validated_data.items():
            if not key == "image":
                postData.setdefault(key, val)

        image = request.FILES.get("image",None)
        obj :UserMembership = UserMembership.objects.create(**postData,user = request.user,image = image)
        
        return MakeResponse({"created" : True})



    def delete(self, request :HttpRequest, id = None ,*args :list , **kwargs: dict) -> HttpResponse:
        queryset :UserMembership = UserMembership.objects.filter(user = request.user).all()
        obj :UserMembership = get_object_or_404(queryset,id = id)
        obj.delete()
        return MakeResponse({"deleted" : True})
    

    def put(self, request :HttpRequest, id = None, *args :list , **kwargs :dict) -> HttpResponse:

        serializer :Serializer = UserMembershipUpdateSerializer(data = request.data,context = {
            "request" : request
        })

        if not serializer.is_valid():
            return MakeResponse(serializer.errors, status = 400)
        
        queryset :UserMembership = UserMembership.objects.filter(user = request.user).all()

        obj :UserMembership = get_object_or_404(queryset,id = id)

        updatedData :dict = {
            "name": serializer.validated_data.get("name", obj.name),
            "rewards" : serializer.validated_data.get("rewards", obj.rewards),
            "welcome_note" : serializer.validated_data.get("welcome_note", obj.welcome_note),
            "description" : serializer.validated_data.get("price_per_month", obj.price_per_month),
            "price_per_year" : serializer.validated_data.get("price_per_year", obj.price_per_year),
            "full_time " : serializer.validated_data.get("price_per_year", obj.price_per_year),
            "max_members" : serializer.validated_data.get("max_members", obj.max_members),
            "limit_members" : serializer.validated_data.get("limit_members", obj.limit_members)

        }

        for key, val in updatedData.items():
            setattr(obj, key, val)
        obj.save()
        
        return MakeResponse({"updated" : True})
        