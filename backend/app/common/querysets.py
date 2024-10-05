from django.db import models
from django.utils import timezone
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
        
        