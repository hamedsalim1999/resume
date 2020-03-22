from django.urls import re_path,path
from . import api



urlpatterns = [
    re_path(r'^v1/$',api.ArticleList.as_view(),name='apitest'),
    re_path(r'^v2/$',api.FormList.as_view(),name='apitest'),
  
    
]
