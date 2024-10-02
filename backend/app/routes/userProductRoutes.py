from ..controllers.userProductsController import UserProductListController
from django.urls import path

userProductListRoutes:list = [
    path("user/product/create",UserProductListController.as_view())
] 