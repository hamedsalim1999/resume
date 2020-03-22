from rest_framework import generics
from resume.serializers import ArticleSerializer , FormSerializer
from resume.models import Article,Form


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
class FormList(generics.ListCreateAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer