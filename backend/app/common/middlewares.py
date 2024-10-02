# from config.settings import SECRET_KEY
# import jwt
# from django.contrib.auth.models import AnonymousUser
# from typing import Any
# from django.http import HttpRequest,HttpResponse
# from ..models.authModels import AuthUserModel
# class C_AuthenticationMiddleware:

#     def __init__(self,get_response:HttpResponse) -> None:

#         self.get_response = get_response 


#     def __call__(self, request:HttpRequest) -> Any:

#         auth_header:str = request.headers.get("Authorization")
#         if not auth_header:
#             request.user = AnonymousUser 
#             response = self.get_response(request)

#             return response 
            
#         token:str = auth_header.split(' ')[1]
        
#         try:
#             payload:dict = jwt.decode(token,SECRET_KEY,algorithms="HS256")
#             print(payload.get("user_id"))
#             user = AuthUserModel.objects.get(id = payload.get("user_id"))
#             print(user)
            
#             request.user = user 
#             print(request.user)
        

#         except:
            
#             request.user = AnonymousUser 

#         response = self.get_response(request)
        
#         return response

        






