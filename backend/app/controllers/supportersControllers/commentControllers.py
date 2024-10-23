from rest_framework.views import APIView 
from ...common.customResponse import MakeResponse
from ...models import UserGalary, UserPost, ProductList , Comment
from ...modules.authManager import C_JWT_SponsorAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import HttpRequest,HttpResponse
from uuid import UUID
from ...serializers.commentSerializers import CommentSerializer
from typing import Any
from django.db import models
from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework.serializers import Serializer
class CommentController(APIView):
    authentication_classes = [C_JWT_SponsorAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request :HttpRequest, id :UUID, *args, **kwargs :dict) -> HttpRequest:
        postsQueries :list = [
                models.Q(draft = False) & models.Q(scheduled = False),
                models.Q(scheduled_for__lt = timezone.now())
            ]
        posts = UserPost.objects.filter(*postsQueries).select_related("user").prefetch_related("images")
        modelTypes :dict = {
            "post" : posts.all(),
            "galary" : UserGalary,
            "product" : ProductList
        }
        if not modelTypes.get(request.GET.get("type")):
            return MakeResponse(
                {
                    "error" : "include type as a get param"
                },
                status=400
            )
        model :Any[UserPost | UserGalary | ProductList] = modelTypes.get(request.GET.get("type"))

        obj :Any[UserPost, UserGalary, ProductList] = get_object_or_404(model, id = id)

        model_object_name = obj.__class__._meta.object_name
        queryset = Comment.objects.filter(object_name = model_object_name).all()
        print(queryset)
        return MakeResponse(queryset.values())
    def post(self, request :HttpRequest, id :UUID = None, *args :list, **kwargs : dict) -> HttpResponse:
        serializer :Serializer = CommentSerializer(data = request.data)
        if not serializer.is_valid():
            return MakeResponse(serializer.errors, status=400)
        postsQueries :list = [
                models.Q(draft = False) & models.Q(scheduled = False),
                models.Q(scheduled_for__lt = timezone.now())
            ]
        posts = UserPost.objects.filter(*postsQueries).select_related("user").prefetch_related("images")
        modelTypes :dict = {
            "post" : posts.all(),
            "galary" : UserGalary,
            "product" : ProductList
        }
        if not modelTypes.get(request.GET.get("type")):
            return MakeResponse(
                {
                    "error" : "include type as a get param"
                },
                status=400
            )
        model :Any[UserPost | UserGalary | ProductList] = modelTypes.get(request.GET.get("type"))

        obj :Any[UserPost, UserGalary, ProductList] = get_object_or_404(model, id = id)

        model_object_name = obj.__class__._meta.object_name

        Comment.objects.create(
            email = request.user.email,
            object_id = obj.id,
            text = serializer.validated_data.get("text"),
            object_name = model_object_name
        )
        return MakeResponse({
            "success" : "commen added"
        })
        





