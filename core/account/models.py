from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # Let us add some simple fields to profile
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=10)


    def __unicode__(self):
        return u"%s" % self.user