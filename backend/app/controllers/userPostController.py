from ..modules.authViews import C_APIView
from django.http import HttpResponse,HttpRequest
from ..serializers.userPostSerializers import UserPostCreateSerializer
from ..common.customResponse import MakeResponse
from rest_framework.serializers import Serializer
from ..models.userPosts import UserPost,Images
from django.db import transaction
class UserPostController(C_APIView):

    @transaction.atomic
    def post(self, request :HttpRequest, *args :list,**kwargs :dict) ->HttpResponse:

        serializer :Serializer = UserPostCreateSerializer(data = request.data)

        if not serializer.is_valid():
            return MakeResponse(data = serializer.errors,status=400)
        

        postData :dict = {}
        
        for key,value in serializer.data.items():
            if key != "images":
                postData.setdefault(key,value)
        
        print(postData)
        images :list = [Images.objects.create(image = img,user = request.user) for img in request.FILES] if request.FILES else []

        user_post :UserPost = UserPost.objects.create(**postData,user = request.user)
        user_post.images.set(images)
        user_post.save()
        # print(images)

        
        
        return MakeResponse({"success":"Post added successfuly"},status=201)

