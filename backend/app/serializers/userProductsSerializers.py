from rest_framework import serializers 
from typing import Union,List
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
