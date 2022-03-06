from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import datetime

# Create your models here.
class Society(models.Model):
    societyName = models.CharField(max_length=64, unique=True)
    # Figure out how to implement properly logo = models.ImageField()
    description = models.CharField(max_length=256)
    # figure out how to do this properly interests = models.EnumField()
    views = models.IntegerField(default=0)
    members = models.IntegerField(default=0)
    
    
    class Meta:
        verbose_name_plural = "Societies"
    
    def __str__(self):
        return self.societyName

class Event(models.Model):
    societyName = models.ForeignKey(Society, on_delete=models.CASCADE)
    eventName = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    members = models.IntegerField(default=0)
    date = models.DateField(default = datetime.date.today())

    def __str__(self):
        return self.eventName
