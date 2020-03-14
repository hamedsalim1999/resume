from django.test import TestCase , client
from .models import Article , Category , Form
from django.utils import timezone

class ArticleModel(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            tittle = 'python',
            slug = 'python-user',
                )
        

        
    def test_Form(self):
        form = Form(
            tittle = 'Q&A',
            message = 'this is test masssage',
            email = 'test@mail.com',
            auther = 'hamed',
        )
        
        form.save()
       

    def test_article(self):
        
        article1 = Article(
            auther = ('F','M' ),
            slug = 'for test example',
            tittle = 'for unit test',
            main_text = ' this is test unit test',
            image = None,
            main_file = None,
        )
        article2 = Article(
            # auther = ('H',),

            slug = 'تست می کنیم',
            tittle = 'برای تست',
            main_text = ' tمتن برای تست است ',
            image = None,
            main_file = None,
            # category_list = self.category,
        )  
        # Article.category_list.objects(self.category)
        article1.save()
        article2.save()
        self.assertLess(article1.published_at,timezone.now())
        