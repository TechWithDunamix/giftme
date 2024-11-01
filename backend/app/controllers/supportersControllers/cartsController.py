from ...common.customResponse import MakeResponse
from ...modules.authManager import C_JWT_SponsorAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.http import HttpRequest, HttpResponse
from ...models import ProductList
from django.shortcuts import get_object_or_404
class CartsController(APIView):
    authentication_classes = [C_JWT_SponsorAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request :HttpRequest, id = None, *args :list, **kwargs :dict) -> HttpResponse:
        product :ProductList = get_object_or_404(ProductList, id = id)
        print(product)
        print(request.user)
        return MakeResponse({"" : ""})

