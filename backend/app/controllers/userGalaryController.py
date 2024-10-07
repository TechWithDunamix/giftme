from ..serializers.userGalarySerializers import UserGalaryCreateSerializer
from ..common.customResponse import MakeResponse 
from ..modules.authViews import C_APIView
from django.http import HttpRequest,HttpResponse
from rest_framework.serializers import Serializer
from ..models.userGalary import UserGalary,Images
from django.db import transaction
class UserGalaryController(C_APIView):
    def validate_images(self,files :list):
        if len(files) > 8:
            return False 
        
        return True
    
    @transaction.atomic
    def post(self, request :HttpRequest, *args :list , **kwargs :dict) ->HttpResponse:

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