from rest_framework import routers, serializers, viewsets
from resume.models import Article , Form

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields =  '__all__'
class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields =  [ 'tittle','message','auther','email']