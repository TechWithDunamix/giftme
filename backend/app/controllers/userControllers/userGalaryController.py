from ...serializers.userGalarySerializers import UserGalaryCreateSerializer,UserGalaryListSerializer,UserGalaryUpdateSerializer
from ...common.customResponse import MakeResponse 
from ...modules.authViews import C_APIView
from django.http import HttpRequest,HttpResponse
from rest_framework.serializers import Serializer
from ...models.userGalary import UserGalary,Images
from django.db import transaction
from django.shortcuts import get_object_or_404
class UserGalaryController(C_APIView):

    #added this validation bcoz drf serializers does't help 
    def validate_images(self,files :list):
        if len(files) > 8:
            return False 
        
        return True
    
    def get(self, request :HttpRequest, id :None = None, *args : list , **kwargs :dict) -> HttpResponse:

        queryset :UserGalary = UserGalary.objects.filter(user = request.user).prefetch_related("images").all()

        if not id :
            
            return MakeResponse(
                paginate=True,
                queryset = queryset,
                request = request,
                serializer = UserGalaryListSerializer
            )
        
        obj :UserGalary = get_object_or_404(queryset,id = id)
        serializer :Serializer = UserGalaryListSerializer(obj,context = {
            "request" : request
        })

        return MakeResponse(serializer.data)


    @transaction.atomic
    def post(self, request :HttpRequest, *args :list , **kwargs :dict) ->HttpResponse:
        print(request.data)
        serializer :Serializer = UserGalaryCreateSerializer(data = request.data)

        if not serializer.is_valid():
            return MakeResponse(serializer.errors,status=400)
        
        if not self.validate_images(request.FILES):
            return MakeResponse({"images" : "Images most not exceed 8"},status = 400)
        
        images :Images = [Images.objects.create(image = img,user = request.user) for img in request.FILES.values()]

        
        
        data :dict = {}

        for key,value in serializer.data.items():

            data.setdefault(key,value)
        galary :UserGalary = UserGalary.objects.create(**data,user = request.user)
        galary.images.set(images)
        galary.save()

        return MakeResponse(serializer.validated_data)
    
    def delete(self, request :HttpRequest,id = None, *args : list ,**kwargs :dict):
        queryset :UserGalary = UserGalary.objects.filter(user = request.user)
        obj :UserGalary = get_object_or_404(queryset,id = id)
        [x.delete() for x in obj.get_image_list()]
        obj.delete()
        return MakeResponse({"deleted" : True})


    def put(self, request :HttpRequest, id = None, *args :list, **kwargs :dict):
        serializer :Serializer = UserGalaryUpdateSerializer(data = request.data)
        if not serializer.is_valid():
            return MakeResponse(serializer.errors,status=400)
        queryset :UserGalary = UserGalary.objects.filter(user = request.user)
        obj :UserGalary = get_object_or_404(queryset,id = id)
        data :dict = {
            "title" : serializer.validated_data.get("title",obj.title),
            "description" : serializer.validated_data.get("description",obj.description),
            "exclusive" : serializer.validated_data.get("exclusive",obj.exclusive),

            
        }
        for key,value in data.items():
            setattr(obj,key,value)
        if len(request.FILES) > 0:
            [x.delete() for x in obj.get_image_list()]
            images :Images = [Images.objects.create(image = img,user = request.user) for img in request.FILES.values()]

            obj.images.set(images)
            
        obj.save()

        return MakeResponse({"edited" : True})


        
