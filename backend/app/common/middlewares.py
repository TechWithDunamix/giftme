from django.http import HttpRequest,HttpResponse

class CORSMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request :HttpRequest):
        response :HttpResponse = self.get_response(request)
        
        response["access-control-allow-origin"] = "http://127.0.0.1:5500"  
        response["access-control-allow-methods"] = "GET, POST, OPTIONS, PUT, DELETE"
        response["Access-Control-Allow-Credentials"] = "true"


        response["Access-Control-Allow-Headers"] = (
            "Authorization, Content-Type, X-Requested-With, Accept, Origin"
        )
        

        if request.method == "OPTIONS":
            response.status_code = 200
            response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS, PUT, DELETE"
            response["Access-Control-Allow-Headers"] = "Authorization, Content-Type"


        return response
