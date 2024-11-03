from ...modules.authViews import C_APIView
from django.http    import HttpRequest,HttpResponse
from ...utils.paystackapi import PaystackCLient
from ...common.customResponse import MakeResponse
from config.settings import PAYSTACK_SECRET
from ...serializers.userPaymentDetailsSerializers import UserPaymentDetailsSerializer
from rest_framework.serializers import Serializer

class PaymentDetailController(C_APIView):

    def post(self, request :HttpRequest, *args :list, **kwargs :dict) -> HttpResponse:
        serializer :Serializer = UserPaymentDetailsSerializer(data = request.data)
        if not serializer.is_valid():
            return MakeResponse(serializer.errors,status=400)
        
        paystack = PaystackCLient(PAYSTACK_SECRET)
        response = paystack.create_subaccount(business_name=request.user.username,
                                   bank_code=serializer.validated_data.get("bank_code","999992"),
                                   account_number=serializer.validated_data.get("account_number")
                                   ,percentage_charge=3)
        
        if response[-1] ==  400:
            return MakeResponse({"error" : "ERR_PAYSTACK","detail":response},status=400)
        
        request.user.account_id = response[0]["data"]["subaccount_code"]
        request.user.save()
        return MakeResponse(response)