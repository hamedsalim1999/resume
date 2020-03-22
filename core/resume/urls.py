from django.urls import re_path,path
from . import views as view



urlpatterns = [
    re_path(r'^hamed$', view.HamedTemplateView.as_view(),name='hamed'),
    re_path(r'^sahand$', view.HamedTemplateView.as_view(),name='sahand'),
    re_path(r'^$', view.HomeTemplateView.as_view(),name='index'),
    re_path(r'^contact$',view.ContactTemplateView.as_view(),name='contact'),
    
    path('<str:uid>',view.ArticleTemplateView.as_view(),name='article'),
    
    
    
]
