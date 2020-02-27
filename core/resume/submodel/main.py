from django.db import models
from django.utils import timezone
class TimeStampedModel(models.Model):
    create = models.DateTimeField(auto_now_add= True)
    update = models.DateTimeField(auto_now= True)
    class Meta:
        abstract = True
class Draft_publish(TimeStampedModel):
    DRAFT ='d'
    PUBLISH = 'p'
    STATUS = (
        (DRAFT,'draft'),
        (PUBLISH,'publish'),
    )
    publish_status = models.CharField(max_length=1,choices=STATUS,default=DRAFT)
    class Meta:
        abstract = True
