from ..modules.authViews import C_APIView
from ..common.customResponse import MakeResponse 
from django.http import HttpRequest,HttpResponse

class UserProductListController(C_APIView):

    def post(self, request:HttpRequest, *args: list,**kwargs:dict) ->HttpResponse:

        return MakeResponse({"success":"sss"})