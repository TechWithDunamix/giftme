from ..modules.authViews import C_APIView
from django.http import HttpResponse,HttpRequest
from ..serializers.userPostSerializers import UserPostCreateSerializer,UserPostListSerializer
from ..common.customResponse import MakeResponse
from rest_framework.serializers import Serializer
from ..models.userPosts import UserPost,Images,PostManager
from typing import Union
from django.db import transaction
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
            serializer :Serializer = UserPostListSerializer(queryset ,many = True,context = context)

            return MakeResponse(
                paginate=True,
                serializer = UserPostListSerializer,
                queryset = queryset,
                request = request
            )


    @transaction.atomic
    def post(self, request :HttpRequest, *args :list,**kwargs :dict) ->HttpResponse:

        serializer :Serializer = UserPostCreateSerializer(data = request.data)

        if not serializer.is_valid():
            return MakeResponse(data = serializer.errors,status=400)
        

        postData :dict = {}
        
        for key,value in serializer.data.items():
            if key != "images":
                postData.setdefault(key,value)
        
        
        
        images :list = [Images.objects.create(image = request.FILES.get("images_0"),user = request.user)]
        
        user_post :UserPost = UserPost.objects.create(**postData,user = request.user)
        user_post.images.set(images)
        user_post.save()
        

        
        
        return MakeResponse({"success":"Post added successfuly"},status=201)

