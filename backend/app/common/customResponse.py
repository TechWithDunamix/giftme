from rest_framework.response import Response 
from typing import Union,Optional
from rest_framework.pagination import PageNumberPagination
from rest_framework.serializers import Serializer
from django.http import HttpRequest
from django.db.models import QuerySet
from ..modules.paginator import paginate_qs
from typing import TypedDict,List,Dict,Any,Union,Optional



class MakeResponseType(TypedDict):
    data :Union[List[dict], Dict[str,any]]
    message :Optional[str]
    paginate :Optional[bool]
    status :Optional[int]
    request :HttpRequest
    serializer :Serializer

class MakeResponse(Response):

    def __init__(self, data=[],message = None,paginate:bool = False, status=200, template_name=None, headers=None, exception=False, content_type=None,**kwargs:MakeResponseType):


        # if not data and paginate == False:
        #     raise ValueError("You can't turn off paginate with no data ")
        meta :dict = {}
        success_status:dict = {
                200: "OK",  # Request succeeded
                201: "Created",  # Resource successfully created
                202: "Accepted",  # Request accepted but not yet processed
                203: "Non-Authoritative Information",  # Returned metadata may be from a third-party source
                204: "No Content",  # Request succeeded but no content to return
                205: "Reset Content",  # Request succeeded, instructing client to reset the view
                206: "Partial Content",  # Partial content returned, typically for range requests
                207: "Multi-Status (WebDAV)",  # Multiple status codes for different operations
                208: "Already Reported (WebDAV)",  # Members already enumerated earlier
                226: "IM Used"  # Response includes 
        }
        if status in success_status.keys():
            status_string:str = "Success"

        else:
            status_string:str = "Error"

        if paginate == True:
            request :HttpRequest = kwargs.get("request")
            _Serializer :Serializer = kwargs.get("serializer")
            queryset :QuerySet = kwargs.get("queryset")
            _paginator,qs =  paginate_qs(request = request,qs=queryset)

            serializer = _Serializer(qs,many = True,context = {
                "request" :  request
            })
            meta :dict = {
                'current_page': _paginator.page.number,          
                'page_size': _paginator.page_size,               
                'total_items': _paginator.page.paginator.count,  
                'total_pages': _paginator.page.paginator.num_pages,  
                'has_next': _paginator.page.has_next(),          
                'has_previous': _paginator.page.has_previous(),  
            }
            data :dict= serializer.data
            

        responseData:dict = {

            "status":status_string,
            "message":message,
            "data" : data,
            "meta" : meta
            

        }
        
        super().__init__(responseData, status, template_name, headers, exception, content_type)


    