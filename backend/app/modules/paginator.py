from rest_framework.pagination import PageNumberPagination 
from rest_framework.serializers import Serializer
from django.http import HttpResponse
def paginate_qs(qs:any = None,request = None,per_page = 6) -> list:
    paginator = PageNumberPagination()
    paginator.page_size = per_page
    paginated_qs = paginator.paginate_queryset(qs,request)
    
    
    
    
    return [paginator,paginated_qs]