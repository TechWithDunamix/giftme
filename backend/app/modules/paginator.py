from rest_framework.pagination import PageNumberPagination 
from rest_framework.serializers import Serializer
from django.http import HttpResponse
def paginate_qs(qs:any = None,serializer:Serializer = None ,request = None,per_page = 5) -> HttpResponse:
    paginator = PageNumberPagination()
    paginator.page_size = per_page
    paginated_qs = paginator.paginate_queryset(qs,request)
    serializer = serializer(paginated_qs,many = True)
    
    return paginator.get_paginated_response(serializer.data)