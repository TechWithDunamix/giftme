from config.settings import SECRET_KEY
import jwt 
from typing import Dict
from .paystackapi import PaystackCLient
# from 
def encode_payment_payload(**payload :Dict[str,str]) -> str:
    return jwt.encode(payload,SECRET_KEY,algorithm="HS256")








