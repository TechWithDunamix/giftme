from ...modules.authViews import C_APIView
from django.http import HttpResponse,HttpRequest
from ...serializers.userPostSerializers import UserPostCreateSerializer,UserPostListSerializer,UserPostUpdateSerializer
from ...common.customResponse import MakeResponse
from rest_framework.serializers import Serializer
from ...models.userPosts import UserPost,Images,PostManager
from typing import Union
from django.db import transaction,models
from django.shortcuts import get_object_or_404
from uuid import UUID
class UserPostController(C_APIView):


    def get(self,request :HttpRequest, id = None ,*args :dict, **kwargs : dict) -> HttpResponse:
        if not id:
            getParams :dict = request.GET

            queryset :Union[PostManager | UserPost] = UserPost.objects.filter(user = request.user).prefetch_related("images").all()


            if getParams.get("draft"):
                queryset :Union[PostManager | UserPost] = UserPost.objects.get_draft.filter(user = request.user)

            
            if getParams.get("published") == "true":
                 queryset :Union[PostManager | UserPost]  = UserPost.objects.get_published.filter(user = request.user).all()

            elif getParams.get("published") == "false"  :
                 queryset :Union[PostManager | UserPost]  = UserPost.objects.get_unpublished.filter(user = request.user).all()
            context :dict = {
                "request" : request
            }

            return MakeResponse(
                paginate=True,
                serializer = UserPostListSerializer,
                queryset = queryset,
                request = request
            )
        
        queryset :models.QuerySet = UserPost.objects.filter(user = request.user)
        obj : UserPost = get_object_or_404(queryset,id = id)
        serializer :Serializer = UserPostListSerializer(obj ,context = {
            "request" : request
        })

        return MakeResponse(serializer.data)



    @transaction.atomic
    def post(self, request :HttpRequest, *args :list,**kwargs :dict) ->HttpResponse:

        serializer :Serializer = UserPostCreateSerializer(data = request.data)

        if not serializer.is_valid():
            return MakeResponse(data = serializer.errors,status=400)
        

        postData :dict = {}
        
        for key,value in serializer.validated_data.items():
            if key != "images":
                postData.setdefault(key,value)
        
        
        images :list = [Images.objects.create(image = request.FILES.get("image"),user = request.user)]
        
        user_post :UserPost = UserPost.objects.create(**postData,user = request.user)
        user_post.images.set(images)
        user_post.save()
        
        return MakeResponse({"success":"Post added successfuly"},status=201)
    
    def put(self,request :HttpRequest,id: UUID = None, *args :list,**kwargs :dict):
        serializer :Serializer = UserPostUpdateSerializer(data = request.data)
        if not serializer.is_valid():
            return MakeResponse(serializer.errors,status = 400)
        queryset :Union[PostManager | UserPost] = UserPost.objects.filter(user = request.user)
        obj :Union[PostManager | UserPost] = get_object_or_404(queryset, id = id)

        postData :dict = {
            "title" : serializer.validated_data.get("title",obj.title),
            "body" : serializer.validated_data.get("body", obj.body),
            "exlusive" : serializer.validated_data.get("exlusive",obj.exlusive),
            "draft" : serializer.validated_data.get("draft",obj.draft),
            "scheduled" : serializer.validated_data.get("scheduled",obj.scheduled),
            "scheduled_for" : serializer.validated_data.get("scheduled_for", obj.scheduled_for)
        }

        for key, value in postData.items():
            setattr(obj,key,value)
        if request.FILES.get("images_0"):
            [x.delete() for x in obj.get_image_list()]
            images = [Images.objects.create(image = request.FILES.get("images_0"),user = request.user)]
            obj.images.set(images)
        obj.save()

        return MakeResponse({"data" : "data"})

    def delete(self,request :HttpRequest,id:UUID = None, *args :list, **kwargs :dict):
        queryset :Union[PostManager | UserPost] = UserPost.objects.filter(user = request.user)
        obj :Union[PostManager | UserPost] = get_object_or_404(queryset, id = id)
        [x.delete() for x in obj.get_image_list()]
        obj.delete()

        return MakeResponse({"Success" : "Deleted"},message="POst deleted sucessfully")

