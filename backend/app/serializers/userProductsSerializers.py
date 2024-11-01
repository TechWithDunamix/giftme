from rest_framework import serializers 
from typing import Union,List,Dict
from ..models.userProducts import ProductList,ProductDiscount
from django.utils import timezone
from django.http import HttpRequest
class UserProductCrationSerializer(serializers.Serializer):
    DEFAULT_SETTING:dict = {
        "quantity" : 100,
        "uer_can_choose_quantity" : True,
        "specs" : {

        }

    }
    name : str = serializers.CharField()

    description : str = serializers.CharField()

    price : Union[int | float] = serializers.FloatField()

    category : List[str] = serializers.ListField(
        child = serializers.CharField()
    )

    image : any  = serializers.ImageField()

    confirmation_massage : str = serializers.CharField(required = False)

    setting : dict =serializers.JSONField(default = DEFAULT_SETTING)

    draft : bool = serializers.BooleanField(default = False)
    free_for_members :bool = serializers.BooleanField()


class UserProductListViewSerializer(serializers.ModelSerializer):
    caterories  :object = serializers.SerializerMethodField()
    class Meta:
        model = ProductList
        fields:list = ["id",'name',"caterories", 'description', 'price', 'image', 'confirmation_massage', 'setting', 'draft']




    
    def get_caterories(self,obj):
        return [x.name for x in obj.category.all()]
    



class UserProductDiscountCreateSerialializers(serializers.Serializer):
    
    title :str = serializers.CharField()

    percentage_or_price :Union[int, float] = serializers.FloatField(required = True)

    starting :str = serializers.DateTimeField(required = False)

    ending :str = serializers.DateTimeField()

    products_ids = serializers.ListField(
        child = serializers.UUIDField()
    )
    limit_quantity :bool = serializers.BooleanField(default = False, required = False)

    max_quantity :str = serializers.CharField(required = False)

    discount_type :str = serializers.CharField()    


    def validate(self, attrs : Dict[str, any]) -> Dict[str, any]:
        discount_type = attrs.get("discount_type")
        starting = attrs.get("starting")
        ending = attrs.get("ending")
        percentage_or_price = attrs.get("percentage_or_price")

        if discount_type not in ["percentage","price"]:
             raise serializers.ValidationError("discount_type must be either 'percentage' or 'price' ")
             
        starting_date = starting or timezone.now()

        if not ending > starting_date:
            raise serializers.ValidationError("Discount end date can not be before start date")

        return attrs
    


class UserProductDiscountListSerialializers(serializers.Serializer):
    id = serializers.UUIDField()
    title :str = serializers.CharField()

    percentage_or_price :Union[int, float] = serializers.FloatField(required = True)

    starting :str = serializers.DateTimeField(required = False)

    ending :str = serializers.DateTimeField()

    limit_quantity :bool = serializers.BooleanField(default = False, required = False)

    max_quantity :str = serializers.CharField(required = False)

    discount_type :str = serializers.CharField() 

    #for extra fields
    def to_representation(self, instance :ProductDiscount):

        data :dict = super().to_representation(instance)
        request :HttpRequest = self.context.get("request")
        data["products"] = [{
                                "image" : request.build_absolute_uri(x["image"]),
                                "name" : x["name"],
                                "id" : x["id"]
                            } for x in instance.products_detail]
        return data

        

       
class UserProductDiscountUpdateSerialializers(serializers.Serializer):

    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        for field_name, field in self.fields.items():
            field.required = False
    
    title :str = serializers.CharField()

    percentage_or_price :Union[int, float] = serializers.FloatField(required = True)

    starting :str = serializers.DateTimeField(required = False)

    ending :str = serializers.DateTimeField()

    products_ids = serializers.ListField(
        child = serializers.UUIDField()
    )
    limit_quantity :bool = serializers.BooleanField(default = False, required = False)

    max_quantity :str = serializers.CharField(required = False)

    discount_type :str = serializers.CharField()    


    def validate(self, attrs : Dict[str, any]) -> Dict[str, any]:
        discount_type = attrs.get("discount_type")
        starting = attrs.get("starting")
        ending = attrs.get("ending")
        percentage_or_price = attrs.get("percentage_or_price")

        if discount_type not in ["percentage","price"]:
             raise serializers.ValidationError("discount_type must be either 'percentage' or 'price' ")
             
        starting_date = starting or timezone.now()

        if not ending > starting_date:
            raise serializers.ValidationError("Discount end date can not be before start date")

        return attrs