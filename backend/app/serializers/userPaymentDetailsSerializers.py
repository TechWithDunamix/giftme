from rest_framework import serializers

class UserPaymentDetailsSerializer(serializers.Serializer):
    bank_code :str = serializers.CharField()
    account_number :str = serializers.CharField()


class UserPaymentDetailsUpdateSerializer(serializers.Serializer):
    bank_code :str = serializers.CharField(required = False)
    account_number :str = serializers.CharField(required = False)
