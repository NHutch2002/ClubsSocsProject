from django import forms
from django.contrib.auth.models import User
from rango.models import Society, Event, UserProfile

# We could add these forms to views.py, but it makes sense to split them off into their own file.

class SocietyForm(forms.ModelForm):
    societyName = forms.CharField(max_length= 64, help_text="Please enter the name of your society.")
    societyName = forms.CharField(max_length= 256, help_text="Please briefly describe your society.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    memberNum = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Society
        fields = ('societyName','logo', 'description')

#class PageForm(forms.ModelForm):
#    title = forms.CharField(max_length=Page.TITLE_MAX_LENGTH, help_text="Please enter the title of the page.")
#    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
#    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
#
#    class Meta:
#        model = Page
#        exclude = ('category',)
#    
#    def clean(self):
#        cleaned_data = self.cleaned_data
#        url = cleaned_data.get('url')
#
#        if url and not url.startswith('http://'):
#            url = f'http://{url}'
#            cleaned_data['url'] = url
#        
#        return cleaned_data

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ()