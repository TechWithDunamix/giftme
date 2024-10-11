from ..controllers import UserProductListController
from django.urls import path

userProductListRoutes:list = [
    path("user/product/create",UserProductListController.as_view()),
    path("user/product/all",UserProductListController.as_view()),
    path("user/product/<uuid:id>",UserProductListController.as_view()),


] 