from typing import Any
from django.db.models import Manager
from django.contrib.auth.models import BaseUserManager 

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
    def filter(self, *args: Any, **kwargs: Any):
        print(kwargs.get("draft"))
        if not kwargs.get("draft"):
            return super().filter(*args, **kwargs)

        options :list = ['true','false']
        
        if kwargs.get("draft") not in options:
            kwargs['draft'] = "false"

        kwargs['draft'] = True if kwargs.get("draft") == "true" else False

        return super().filter(*args, **kwargs)