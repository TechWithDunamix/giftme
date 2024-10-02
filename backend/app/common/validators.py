from django.core.exceptions import ValidationError
from django.utils import crypto

class AuthValidators:

    def validate_first_name(self,value:str) -> str:
        return value.upper()
    

    def validate_last_name(self,value:str) -> str:
        return value.upper()


    