import httpx
from asgiref.sync import async_to_sync
from config.settings import PAYSTACK_SECRET
class PaystackSync:
    def __init__(self, secret_key):
        self.base_url = "https://api.paystack.co"
        self.secret_key = PAYSTACK_SECRET
        self.headers = {
            "Authorization": f"Bearer {self.secret_key}",
            "Content-Type": "application/json"
        }

    async def _create_subaccount_async(self, business_name, bank_code, account_number, percentage_charge):
        url = f"{self.base_url}/subaccount"
        data = {
            "business_name": business_name,
            "bank_code": bank_code,
            "account_number": account_number,
            "percentage_charge": percentage_charge
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=data, headers=self.headers)
        return response.json()

    def create_subaccount(self, business_name, bank_code, account_number, percentage_charge):
        """
        Synchronous wrapper for creating a subaccount.
        """
        return async_to_sync(self._create_subaccount_async)(business_name, bank_code, account_number, percentage_charge)

    async def _initialize_payment_async(self, email, amount, callback_url, metadata=None):
        url = f"{self.base_url}/transaction/initialize"
        data = {
            "email": email,
            "amount": amount,
            "callback_url": callback_url,
            "metadata": metadata or {}
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=data, headers=self.headers)
        return response.json()

    def initialize_payment(self, email, amount, callback_url, metadata=None):
        """
        Synchronous wrapper for initializing a payment.
        """
        return async_to_sync(self._initialize_payment_async)(email, amount, callback_url, metadata)

    async def _verify_payment_async(self, reference):
        url = f"{self.base_url}/transaction/verify/{reference}"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers)
        return response.json()

    def verify_payment(self, reference):
        """
        Synchronous wrapper for verifying a payment.
        """
        return async_to_sync(self._verify_payment_async)(reference)

    # Add more methods for other functionalities similarly...
