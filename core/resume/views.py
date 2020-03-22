from django.shortcuts import render
from django.contrib import messages
from rest_framework import generics
from django.shortcuts import render , redirect
from django.views.generic import TemplateView,ListView,DetailView
from django.http import HttpResponse
from .models import Article
from .forms import SendForm
from .serializers import ArticleSerializer
class HamedTemplateView(TemplateView):
    template_name = 'index.html'
    page_name = 'Hamed'

class HomeTemplateView(ListView):
    template_name = 'post.html'
    page_name = 'home'
    model = Article
    context_object_name = 'post_show'
class ArticleTemplateView(DetailView):
    template_name = 'post.html'
    page_name = 'post'
    pk_url_kwarg = 'uid'
    model = Article
    context_object_name = 'article_detail'

class ContactTemplateView(TemplateView):
    template_name = 'contact.html'
    page_name = 'contact'
    def get(self,request):
        
        form = SendForm()
        context = {
            'form':form
        }
        return render(request,self.template_name,context)

        
    def post(self,request):
        form = SendForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS , "thanks for submitting a message ")
            return redirect('contact')
        messages.add_message(request,messages.ERROR , 'we cand submitting a massage sorry :(')
        return redirect('contact')
class ArticleView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    