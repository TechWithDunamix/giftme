from django.db import models
from typing import Iterable, Union,List
from .authModels import AuthUserModel
from django.db import transaction
from .bases import C_BaseModels
from ..common.managers import ProductListManager
from django.db.models import Manager
from .sponsors import Sponsors
from django.utils import timezone


class Category(C_BaseModels):
    name:str = models.CharField(max_length=150)

class ProductList(C_BaseModels):

    objects:Manager = ProductListManager()
    
    user :AuthUserModel = models.ForeignKey(AuthUserModel,related_name="user_products",on_delete=models.CASCADE,null=True)

    name:str = models.CharField(max_length=150)

    description:str = models.TextField()

    price:Union[int | float] = models.DecimalField(decimal_places=2,max_digits=9)

    category:models.ManyToManyField = models.ManyToManyField(Category,related_name="products")

    image:models.ImageField = models.ImageField(upload_to="product_images")

    confirmation_massage:str = models.TextField(default="Product ordered !!!")

    setting:dict = models.JSONField(default=dict)

    draft:bool = models.BooleanField(default=False)

    class Meta:
        db_table = "Products"


    def __str__(self) -> str:
            return self.name
    
    @transaction.atomic
    def save(self, **kwargs:dict) -> None:
         self.name = self.name.upper()
         self.price = float(self.price)
         
         return super().save(**kwargs)
    
    @transaction.atomic
    def delete(self,**kwargs) -> tuple[int, dict[str, int]]:
         if self.image:
              self.image.delete()
         return super().delete(**kwargs)
    class Meta:
         ordering = ["-date_created"]
         db_table = "Product"


class ProductSales(C_BaseModels):

    product = models.ForeignKey(ProductList, related_name="sales", on_delete = models.CASCADE)
    sponsor  = models.ForeignKey(Sponsors, related_name="buys", on_delete = models.CASCADE)

    @transaction.atomic
    def save(self, **kwargs :dict) -> None:
        return super().save(**kwargs)
    

class ProductDiscount(C_BaseModels):
     
     title :str = models.CharField(max_length=120)

     percentage_or_price :Union[int, float] = models.FloatField()

     starting = models.DateTimeField(default=timezone.now())

     ending = models.DateTimeField(null=True)

     products :ProductList = models.ManyToManyField(ProductList, related_name = "discounts")

     limit_quantity:bool = models.BooleanField(default=False)

     max_quantity :Union[int, float]  = models.PositiveSmallIntegerField(null=True)

     discount_type :str = mo
     @transaction.atomic
     def save(self, **kwargs :dict) -> None:
        return super().save(**kwargs)


     
     