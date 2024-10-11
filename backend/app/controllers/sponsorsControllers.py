from ..common.customResponse import MakeResponse
from ..modules.authViews import APIView
from django.http import HttpRequest,HttpResponse
from ..models.sponsors import Sponsors
from rest_framework.permissions import AllowAny
from ..serializers.sponsorsSerializers import SponsorCreateSerializer
from rest_framework.serializers import Serializer
class SponsorCreationController(APIView):
    permission_classes = [AllowAny]


    def post(self, request :HttpRequest, *args : list, **kwargs : dict) -> HttpResponse:

        serializer :Serializer = SponsorCreateSerializer(data = request.data)

        if not serializer.is_valid():
            return MakeResponse(serializer.errors, status=400)
        
        email :str = serializer.validated_data.get("email")
        sponsor  = Sponsors.get_or_create(email = email)

        print(sponsor.otp)
        print(sponsor.date_created)

        
        

        return MakeResponse({"created" :True}, status=201)

