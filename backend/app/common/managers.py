from django.db.models import manager
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


