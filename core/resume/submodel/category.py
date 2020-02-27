from django.db import models
from .main import Draft_publish
from django.utils import timezone
import uuid
class Category(models.Model):
    tittle = models.CharField(max_length=256, db_index=True, unique=True)
    slug = models.SlugField(max_length=128,unique=True)
    def __str__(self):
        return self.tittle