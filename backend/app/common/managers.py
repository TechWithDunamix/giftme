from typing import Any
from django.db.models import Manager
from django.contrib.auth.models import BaseUserManager 
from django.db.models import Q,QuerySet
from .querysets import PostListQuerysets,ProductDiscountQuerySet,ProductListQuerySet
class UserManager(BaseUserManager):

     def create_user(self,email:str, password: str,username:str,last_name:str,first_name: str,country:str) -> object:

        if not email:
            raise ValueError("'Email' is required")
        
        if not password:
            raise ValueError("'Password' is required")
        
        if not username:
            raise ValueError("' Username' is a required field")
        
        if not last_name:
            raise ValueError(" 'Last name' is a required field")
        
        if not first_name:
            raise ValueError("' First name '  a required field")
        
        if not country:
            raise ValueError(" 'Country'  is a required fuield")

        user_object =  self.create(
            email = email,
            username = username,
            last_name =last_name,
            first_name = first_name,
            country = country
        )

        user_object.set_password(password)
        user_object.save(using = self._db)
        
        return user_object




class ProductListManager(Manager):
    def get_queryset(self) -> ProductListQuerySet:
        return ProductListQuerySet(self.model, using=self._db)
    def filter_draft(self, *args: Any, **kwargs: Any):

        
        if not kwargs.get("draft"):
            del kwargs['draft']
            return super().filter(*args, **kwargs)

        options :list = ['true','false']
        
        if kwargs.get("draft") not in options:
            kwargs['draft'] = "false"

        kwargs['draft'] = True if kwargs.get("draft") == "true" else False

        return super().filter(*args, **kwargs)
      
    
    def get_top_products(self) -> "ProductListManager":
        return self.get_queryset().get_top_products().distinct()
    

class PostManager(Manager):

    def get_queryset(self) -> PostListQuerysets:
        return PostListQuerysets(self.model,using=self._db)
    

    @property
    def get_draft(self) -> QuerySet:

        return self.get_queryset().get_all(draft=True)
    
    @property
    def get_published(self,**kwargs : dict) -> QuerySet:

        return self.get_queryset().get_published(published = True)
    
    @property
    def get_unpublished(self, **kwargs : dict) ->QuerySet:
        return self.get_queryset().get_published(published = False)


    
class ProductDiscountManager(Manager):

    def get_queryset(self) -> ProductDiscountQuerySet:
        return ProductDiscountQuerySet(self.model,using=self.db)
    

    @property
    def get_active(self):
        return self.get_queryset().get_active().all()
  
        
    