from rest_framework import serializers
from typing import Dict
from ..models import CartItems,ProductList
from django.http import HttpRequest
class CartSerializer(serializers.Serializer):
    product = serializers.SerializerMethodField()
    shop = serializers.SerializerMethodField()
    date_created = serializers.DateTimeField()

    def get_product(self, instace :CartItems) -> Dict[str,str]:
        request :HttpRequest = self.context.get("request")
        product :ProductList = instace.products

        #TODO Add has_discount_field
        return {
            "id" :product.id,
            "name" : product.name,
            "image" : request.build_absolute_uri(product.image.url)

        }
    
    def get_shop(self,  instace :CartItems) -> Dict[str,str]:
        request :HttpRequest = self.context.get("request")
        shop = instace.shop

        return {
            "id" : shop.id,
            "name" : shop.username,
        }
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['id'] = instance.id
        return data

        

