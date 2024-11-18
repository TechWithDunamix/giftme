from ...common.customResponse import MakeResponse
from ...modules.authManager import C_JWT_SponsorAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.serializers import Serializer
from django.http import HttpRequest, HttpResponse
from ...models import ProductList,CartItems,Sponsors
from ...serializers.cartSerializer import CartSerializer
from django.shortcuts import get_object_or_404
class CartsController(APIView):
    authentication_classes = [C_JWT_SponsorAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request :HttpRequest, id = None, *args :list, **kwargs :dict):
        query_set = CartItems.objects.filter(owner__email = request.user.email)
        if request.GET.get("shop_id"):
            query_set = query_set.filter(shop__id = request.GET.get("shop_id"))

        serializer :Serializer = CartSerializer(query_set,many = True, context = {
            "request" : request
        })
        return MakeResponse(serializer.data)

    def post(self, request :HttpRequest, id = None, *args :list, **kwargs :dict) -> HttpResponse:
        product :ProductList = get_object_or_404(ProductList.objects.filter(draft = False), id = id)
        owner = Sponsors.get_or_create(email = request.user.email)
        CartItems.objects.create(owner = owner, shop = product.user,products = product )
        return MakeResponse({"sucess" : "product added successfuly"})

    def delete(self,request :HttpRequest, id = None, *args :list, **kwargs :dict) -> HttpResponse:
        query_set = CartItems.objects.filter(owner__email = request.user.email)
        obj :CartItems = get_object_or_404(query_set, id = id)
        obj.delete()
        return MakeResponse({"deleted":"True"})
        