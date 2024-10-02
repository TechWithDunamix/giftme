from rest_framework.response import Response 
from typing import Union,Optional
class MakeResponse(Response):

    def __init__(self, data=None,message = None, status=200, template_name=None, headers=None, exception=False, content_type=None):

        
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
            
        responseData:dict = {
            "status":status_string,
            "message":message,
            "data" : data

        }
        
        super().__init__(responseData, status, template_name, headers, exception, content_type)