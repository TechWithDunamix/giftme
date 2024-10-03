from ..modules.authViews import C_APIView
from ..common.customResponse import MakeResponse 
from django.http import HttpRequest,HttpResponse
from ..serializers.userProductsSerializers import UserProductCrationSerializer,UserProductListViewSerializer
from rest_framework.serializers import Serializer
from ..models.userProducts import ProductList,Category
import json
from django.db import transaction
from django.db.models import QuerySet
class UserProductListController(C_APIView):
    def get(self,request:HttpRequest,id = None,*args :list, **kwargs :dict) ->HttpResponse:
        draft :bool = request.GET.get("draft")

        querySetList: QuerySet = ProductList.objects.filter(user = request.user,draft = draft) \
                                 .prefetch_related("category").all()
        
        serializer :Serializer = UserProductListViewSerializer(querySetList,many = True)
        return MakeResponse(serializer.data)
    @transaction.atomic
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

        product:ProductList = ProductList.objects.create(**productData,user = request.user)
        product.category.set(category)
        return MakeResponse({"success":"Product added success"},status = 201)
    


