from django.urls import path
from ..controllers.supportersControllers.productPurchase import InializeProductPurchase
payment_routes = [
    path("payment/product/<uuid:id>",InializeProductPurchase.as_view())
]