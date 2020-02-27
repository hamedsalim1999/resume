from django.urls import re_path,path
from . import views as view



urlpatterns = [
    re_path(r'^hamed$', view.HamedTemplateView.as_view()),
    re_path(r'^sahand$', view.HamedTemplateView.as_view()),
    re_path(r'^$', view.HomeTemplateView.as_view()),
    path('<str:uid>',view.ArticleTemplateView.as_view()),
    
    
    
]
