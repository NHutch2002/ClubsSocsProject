from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import datetime

# Create your models here.

#Should we have a OneToOne relationship with User in Society, because there are society users? Ask tutor if possible
class Society(models.Model):
    societyName = models.CharField(max_length=64, unique=True)
    logo = models.ImageField(upload_to='society_logos', blank = True)
    description = models.CharField(max_length=256)
    # figure out how to do this properly interests = models.EnumField()
    views = models.IntegerField(default=0)
    members = models.IntegerField(default=0)
    slug = models.SlugField(unique = True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.societyName)
        super(Society,self).save(*args,**kwargs)

    
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
    slug = models.SlugField(unique = True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.eventName)
        super(Event,self).save(*args,**kwargs)

    def __str__(self):
        return self.eventName

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    #username, first name, last name, email, and password fields all provided by User model by default
    # figure out how to do this properly interests = models.EnumField()
    is_society = models.BooleanField()

    def __str__(self):
        return self.user.username    