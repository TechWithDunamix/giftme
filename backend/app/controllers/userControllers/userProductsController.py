from ...modules.authViews import C_APIView
from ...common.customResponse import MakeResponse 
from django.http import HttpRequest,HttpResponse
from ...serializers.userProductsSerializers import UserProductCrationSerializer,UserProductListViewSerializer
from rest_framework.serializers import Serializer
from ...models.userProducts import ProductList,Category
import json
from django.db import transaction
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404
from typing import Any
class UserProductListController(C_APIView):
    def get(self,request:HttpRequest,id = None,*args :list, **kwargs :dict) ->HttpResponse:
        if not id:
            draft :bool = request.GET.get("draft")

            querySetList: QuerySet = ProductList.objects.filter_draft(user = request.user,draft = draft) \
                                    .prefetch_related("category").all()
            
           
        
           
            return MakeResponse(
                                paginate=True,
                                
                                request = request,
                                serializer = UserProductListViewSerializer,
                                queryset = querySetList
                                )
            
        
        querySetList :QuerySet = get_object_or_404(
            ProductList.objects.filter(user = request.user),
            id = id
        )

        serializer :Serializer = UserProductListViewSerializer(querySetList)


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
    
    def delete(self,request :HttpRequest,id :Any = None,*args :list, **kwargs :dict) ->HttpResponse:
        userProducts :QuerySet = ProductList.objects.filter(user = request.user)
        _object :ProductList = get_object_or_404(userProducts,id = id)
        _object.delete()
        return MakeResponse({"success" : "Deleted"})
    

    def put(self,request :HttpRequest,id :Any = None,*args :list, **kwargs :dict) ->HttpResponse:
        serializer :Serializer = UserProductCrationSerializer(data = request.data)
        if not serializer.is_valid():
            return MakeResponse(serializer.errors,status=400)
        userProducts :QuerySet = ProductList.objects.filter(user = request.user)
        _object :ProductList = get_object_or_404(userProducts,id = id)
        _object_data :dict =  {
            "name" : serializer.validated_data.get("name",_object.name),
            "description" : serializer.validated_data.get("description",_object.description),
            "price" : serializer.validated_data.get("price",_object.price),
            "image" : request.FILES.get("image",_object.image),
            "confirmation_massage" : serializer.validated_data.get("prconfirmation_massageice",_object.confirmation_massage),
            "setting"   :serializer.validated_data.get("setting",_object.setting),
            "draft" : serializer.validated_data.get("draft",_object.draft)
        }
        categories: dict = _object.category.all()

        if serializer.validated_data.get("category"):
            categories: dict = [Category.objects.get_or_create(name = x)[0] for x in json.loads(serializer.validated_data.get("category")[0])]
        
        for key,value in _object_data.items():
            setattr(_object,key,value)

        _object.category.set(categories)

        _object.save()


        return MakeResponse({"succes" : "updated"})