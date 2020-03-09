from django.db import models
from django.utils import timezone
class Form (models.Model):
    tittle = models.CharField(max_length=256)
    message = models.TextField()
    auther = models.CharField(max_length=128)
    published_at = models.DateTimeField(default = timezone.now)
    email = models.EmailField()
    ISread = models.BooleanField(default= False)
    class Meta:
        ordering = ['-published_at']
        verbose_name = 'Form'
        verbose_name_plural = 'Forms'