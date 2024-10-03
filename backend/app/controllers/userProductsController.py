from ..modules.authViews import C_APIView
from ..common.customResponse import MakeResponse 
from django.http import HttpRequest,HttpResponse
from ..serializers.userProductsSerializers import UserProductCrationSerializer
from rest_framework.serializers import Serializer
from ..models.userProducts import ProductList,Category
import json
class UserProductListController(C_APIView):

    def post(self, request:HttpRequest, *args: list,**kwargs:dict) ->HttpResponse:
        serializer:Serializer = UserProductCrationSerializer(data = request.data)

        if not serializer.is_valid():
            return MakeResponse(serializer.errors,status=400)
        
        productData :dict  = {}
        for key,value in serializer.data.items():
            if key !="image" and key !="category":
                productData.setdefault(key,value)

      
        productData.setdefault("image",request.FILES.get("image"))

        
        

        categoryJSON:json.JSONDecoder = json.loads(serializer.data.get("category")[0])
        category:Category = [Category.objects.get_or_create(name = names)[0] for names in categoryJSON]

        product:ProductList = ProductList.objects.create(**productData)
        product.category.set(category)
        return MakeResponse({"success":"Product added success"})
    

