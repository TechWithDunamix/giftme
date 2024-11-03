from ..controllers.userControllers.PaymentDetailsControllers import PaymentDetailController
from django.urls import path


userpaymentdetailsroutes = [
    path("user/payment",PaymentDetailController.as_view())
]