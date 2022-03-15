from django import forms
from django.contrib.auth.models import User
from rango.models import Society, Event, UserProfile

# We could add these forms to views.py, but it makes sense to split them off into their own file.

class SocietyForm(forms.ModelForm):
    societyName = forms.CharField(max_length= 64)
    description = forms.CharField(max_length= 256)
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    memberNum = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Society
        fields = ('societyName','logo', 'description')

class EventForm(forms.ModelForm):
    eventName = forms.CharField(max_length=64)
    description = forms.CharField(max_length=256)
    memberNum = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Event
        exclude = ('society', 'attendee')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)