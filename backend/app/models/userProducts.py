from django.db import models
from typing import Iterable, Union,List
from .authModels import AuthUserModel
from django.db import transaction
from .bases import C_BaseModels
from ..common.managers import ProductListManager
from django.db.models import Manager
from .sponsors import Sponsors
from django.utils import timezone
from django.core.exceptions import ValidationError
from ..common.managers import ProductDiscountManager
from django.db.models.manager import Manager
import uuid
from typing import Dict
Shops = AuthUserModel
class Category(C_BaseModels):
    name:str = models.CharField(max_length=150)

class ProductList(C_BaseModels):

    objects:   Manager = ProductListManager()
    
    user :AuthUserModel = models.ForeignKey(AuthUserModel,related_name="user_products",on_delete=models.CASCADE,null=True)

    name:str = models.CharField(max_length=150)

    description:str = models.TextField()

    price:Union[int | float] = models.DecimalField(decimal_places=2,max_digits=9)

    category:models.ManyToManyField = models.ManyToManyField(Category,related_name="products")

    image:models.ImageField = models.ImageField(upload_to="product_images")

    confirmation_massage:str = models.TextField(default="Product ordered !!!")

    setting:dict = models.JSONField(default=dict)

    draft:bool = models.BooleanField(default=False)

    free_for_members :bool = models.BooleanField(default=False)

    file  = models.FileField(upload_to="products/files",null=True)

    spec :Dict = models.JSONField(default=dict)


    class Meta:
        db_table = "Products"


    def __str__(self) -> str:
            return self.name
    
    @transaction.atomic
    def save(self, **kwargs:dict) -> None:
         self.name = self.name.upper()
         self.price = float(self.price)
         self.save_setting(self.setting)
         if self.file:
          product_file_type = self.file.name.split(".")[-1]

          self.file.name = f"{uuid.uuid4()}.{product_file_type}"
         if self.image:
          
          product_image_type = self.image.name.split(".")[-1]

          self.image.name = f"{uuid.uuid4()}.{product_image_type}"

         
         return super().save(**kwargs)
    
    @transaction.atomic
    def delete(self,**kwargs) -> tuple[int, dict[str, int]]:
         if self.image:
              self.image.delete()
         if self.file:
              self.file.delete()
         return super().delete(**kwargs)
    
    def save_setting(self, values :Dict[str,any]):
        DEFAULT_SETTING = {
            "quantity" : None,
            "allow_qty" : False,
            
        }

        UDPDATED_SETTING = {
            "quantity" : values.get("quantity",DEFAULT_SETTING['quantity']),
            "allow_qty" : values.get("allow_qty",DEFAULT_SETTING['allow_qty']),
            
        }
        self.setting = UDPDATED_SETTING


    class Meta:
         ordering = ["-date_created"]
         db_table = "Product"



    

class ProductDiscount(C_BaseModels):
     user = models.ForeignKey(AuthUserModel, related_name="discount", on_delete=models.CASCADE,null = True)
     title :str = models.CharField(max_length=120)

     percentage_or_price :Union[int, float] = models.FloatField()

     starting = models.DateTimeField(default=timezone.now)

     ending = models.DateTimeField(null=True)

     products :Union[models.ManyToManyField] = models.ManyToManyField(ProductList, related_name = "discounts")

     limit_quantity:bool = models.BooleanField(default=False)

     max_quantity :Union[int, float]  = models.PositiveSmallIntegerField(null=True)

     discount_type :str = models.CharField(max_length = 250, default="percentage")

    
     @transaction.atomic
     def save(self, **kwargs :dict) -> None:
        return super().save(**kwargs)
     

     @property
     def products_detail(self):
          qs = self.products.values("name","image","id")
          return qs



        
       
     query :ProductDiscountManager = ProductDiscountManager()
     objects = Manager()




class CartItems(C_BaseModels):
     owner :Sponsors = models.ForeignKey(Sponsors, related_name="cartItems", on_delete=models.CASCADE)

     shop :Shops = models.ForeignKey(Shops, related_name="orders", on_delete=models.CASCADE)

     products :ProductList = models.ForeignKey(ProductList, related_name="product_sales", on_delete=models.CASCADE)

     ordered :bool = models.BooleanField(default=False)

     delivered :bool = models.BooleanField(default=False)

     class Meta:
          db_table = "Cart Items"



class ProductSales(C_BaseModels):

    product = models.ForeignKey(ProductList, related_name="all_sales", on_delete = models.CASCADE)
    sponsor  = models.ForeignKey(Sponsors, related_name="buys", on_delete = models.CASCADE)

    @transaction.atomic
    def save(self, **kwargs :dict) -> None:
        return super().save(**kwargs)