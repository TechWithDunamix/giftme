from django.db.models import manager
from django.contrib.auth.models import BaseUserManager 

class UserManager(BaseUserManager):

     def create_user(self,email:str, password: str,username:str,last_name:str,first_name: str) -> object:

        user_object =  self.create(
            email = email,
            username = username,
            last_name =last_name,
            first_name = first_name
        )

        user_object.set_password(password)
        user_object.save(using = self._db)
        
        return user_object


