from ..controllers.supportersControllers.cartsController import CartsController

from django.urls import path

carts_routes = [
    path("cart/add/<uuid:id>",CartsController.as_view()),
    path("cart",CartsController.as_view()),
    path("cart/delete/<uuid:id>",CartsController.as_view())



]