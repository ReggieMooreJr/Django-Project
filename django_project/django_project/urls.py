import blog
from django.contrib import admin
from django.urls import path, include
from django_project.views import index, miko, milani, searchpage, familymatters


urlpatterns = (
    path('admin/', admin.site.urls),
    path('index/', index),
    path('miko/', miko),
    path('searchpage', searchpage),
    path('milani/', milani),
    path('familymatters/', familymatters),
    path('', include ('blog.urls')),
)
