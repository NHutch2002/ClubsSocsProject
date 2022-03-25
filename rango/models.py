from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import datetime

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    #username, first name, last name, email, and password fields all provided by User model by default
    is_society = models.BooleanField(default = False);
    is_student = models.BooleanField(default = False);
    
    picture = models.ImageField(upload_to='profile_pictures', blank = True)
    

    def __str__(self):
        return self.user.username   

#Should we have a OneToOne relationship with User in Society, because there are society users? Ask tutor if possible
class Society(models.Model):
    owner = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null = True) #One to one relationship defining a user who owns the society.
    member = models.ManyToManyField(UserProfile, related_name = "memberOf", null = True) #Many to many relationship to enable identifiaction of what regular users are members of this society
    societyName = models.CharField(max_length=64, unique=True)
    logo = models.ImageField(upload_to='society_logos', default = 'avatar.png')
    description = models.CharField(max_length=256)
    views = models.IntegerField(default=0)
    memberNum = models.IntegerField(default=0)
    slug = models.SlugField(unique = True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.societyName)
        super(Society,self).save(*args,**kwargs)

    
    class Meta:
        verbose_name_plural = "Societies"
    
    def __str__(self):
        return self.societyName

class Event(models.Model):
    society = models.ForeignKey(Society, on_delete=models.CASCADE)
    attendee = models.ManyToManyField(UserProfile, null = True) #Many to many relationship to enable identifiaction of what regular users are attending this event
    eventName = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    memberNum = models.IntegerField(default=0)
    date = models.DateField(default = datetime.date.today())
    slug = models.SlugField(unique = True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.eventName)
        super(Event,self).save(*args,**kwargs)

    def __str__(self):
        return self.eventName 