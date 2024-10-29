from ..controllers import UserProductListController,UserProductsDiscountController
from django.urls import path

userProductListRoutes:list = [
    path("user/product/create",UserProductListController.as_view()),
    path("user/product/all",UserProductListController.as_view()),
    path("user/product/<uuid:id>",UserProductListController.as_view()),
    path("user/product/discount",UserProductsDiscountController.as_view()),
    path("user/product/discount/<uuid:id>",UserProductsDiscountController.as_view())



] 


