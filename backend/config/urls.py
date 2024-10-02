
from django.contrib import admin
from django.urls import path,include 
from . import settings
from django.conf.urls.static import static
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/",include('app.routes'))
]


urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
