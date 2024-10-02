from ..models.authModels import AuthUserModel 
from typing import Union
import uuid
import jwt
import datetime
from config.settings import SECRET_KEY
class AuthenticationCheck:

    def authenticate(self,email:str = None,password: str = None) -> Union[AuthUserModel | None]:
        try:
            user = AuthUserModel.objects.get(email = email)
        except AuthUserModel.DoesNotExist:
            return None 
        
        if user.check_password(password):
            return user 
        
        return None 





def make_token(user_id:uuid.UUID) -> str:
    payload:dict = {
        "user_id":str(user_id),
        "exp":datetime.datetime.utcnow() + datetime.timedelta(days=7)
    }

    return jwt.encode(payload,SECRET_KEY,algorithm="HS256")




