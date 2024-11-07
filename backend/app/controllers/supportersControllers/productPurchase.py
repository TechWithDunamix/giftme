from ...common.customResponse import MakeResponse
from rest_framework.permissions import IsAuthenticated
from ...modules.authManager import C_JWT_SponsorAuthentication 
from rest_framework.views import APIView
from django.http import HttpRequest,HttpResponse
from django.shortcuts import get_object_or_404
from ...utils.paystackapi import PaystackCLient
from ...models.userProducts import ProductList
from config.settings import PAYSTACK_SECRET

class InializeProductPurchase(APIView):
    paystck = PaystackCLient()
    authentication_classes = [C_JWT_SponsorAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request :HttpResponse, id = None, *args :list , **kwargs :dict) -> HttpResponse:
        product = get_object_or_404(ProductList,id = id)
        print(product.user.account_id)
        resposne = self.paystck.initialize_payment(request.user.email,
                                        amount=product.price,callback_url="google.com",
                                        subaccount=product.user.account_id)
        
        return MakeResponse(resposne)

    