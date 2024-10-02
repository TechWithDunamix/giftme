from rest_framework.views import APIView 
from django.http import HttpRequest
from ..common.customResponse import MakeResponse
from django.http.response import HttpResponseForbidden
import json
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
class C_APIView(APIView):
   authentication_classes = [TokenAuthentication]
   permission_classes = [IsAuthenticated]

   def dispatch(self, request:HttpRequest, *args, **kwargs):
         
      return super().dispatch(request, *args, **kwargs)