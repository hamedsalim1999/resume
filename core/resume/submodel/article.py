from django.db import models
from django.utils import timezone
import uuid
from .main import Draft_publish
from multiselectfield import MultiSelectField
class Article(Draft_publish):
    Auther_LIST = (
        ('H','hamed' ),
        ('S','sahand' ),
         )
    auther = MultiSelectField(choices = Auther_LIST, max_length=3)
    uid = models.UUIDField(primary_key= True , default= uuid.uuid4 , editable=False)
    slug = models.CharField(max_length=128,db_index=True,unique=True)
    tittle = models.CharField(max_length=256, db_index=True ,unique_for_date='published_at' )
    published_at = models.DateTimeField(default = timezone.now)
    main_text = models.TextField()
    image = models.ImageField(upload_to='post',blank=True, null=True , help_text='uplaod image',width_field='width_field', height_field='height_field')
    width_field  = models.PositiveIntegerField(null = True , blank = True , default = '1080')
    height_field = models.PositiveIntegerField(null = True , blank = True , default = '720')
    category_list = models.ManyToManyField('resume.Category')
    main_file = models.FileField(upload_to='resume_file',blank=True, null=True)
    def __str__(self):
        return self.tittle 
    def published_post(self):
        return self.get_queryset().filter(publish_status = 'p').ordering_by('-published_at')
    def published_post(self):
        return self.get_queryset().filter(publish_status = 'd').ordering_by('-published_at')
    def __repr__(self):
        self.category_list
    class Meta:
        ordering = ['-published_at']
        verbose_name = 'article'
        verbose_name_plural = 'articles'
