from rest_framework import serializers 
from typing import Union,List
from ..models.userProducts import ProductList
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


class UserProductListViewSerializer(serializers.ModelSerializer):
    caterories  :object = serializers.SerializerMethodField()
    class Meta:
        model = ProductList
        fields:list = ["id",'name',"caterories", 'description', 'price', 'image', 'confirmation_massage', 'setting', 'draft']




    
    def get_caterories(self,obj):
        return [x.name for x in obj.category.all()]
    

