""
from django.contrib import admin
from django.urls import path,include
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.home,name="home"),
    path("module1/",views.module1,name="module1"),
    path("module2/",views.module2,name="module2"),
     path("module3/",views.module3,name="module3"),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

