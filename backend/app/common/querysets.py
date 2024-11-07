from django.db import models
from django.utils import timezone
from django.db.models import Case,When,BooleanField
class PostListQuerysets(models.QuerySet):
    def get_all(self,draft:bool = True) -> models.QuerySet:
        if isinstance(draft,bool):
            return self.filter(draft = draft)
        return self.all()
    
    def get_published(self,**kwargs :dict) -> models.QuerySet:
        if kwargs.get("published") == True:
            query:models.Q = models.Q(scheduled_for__lt = timezone.now()) & models.Q(draft = False)

        if kwargs.get("published") == False:
            query:models.Q = models.Q(scheduled_for__gt = timezone.now()) & models.Q(scheduled = True)

        return self.filter(query).all()
    


class ProductDiscountQuerySet(models.QuerySet):
    def get_active(self, **kwargs: dict):
        query :models.Q = models.Q(ending__gt = timezone.now())
        return self.filter(query).all()
        
        
class ProductListQuerySet(models.QuerySet):
     
     def get_top_products(self):
        from ..models.authModels import AuthUserModel

        #imported this here to avoint circuler import

        top_users = AuthUserModel.get_top_users().distinct().values_list("id",flat=True)
        return self.filter(draft = False).annotate(is_top_product = Case(
            When(user_id__in = top_users, then=True),
            default=False,
            output_field=BooleanField()
        )).order_by("-is_top_product").order_by("-date_created")
    
