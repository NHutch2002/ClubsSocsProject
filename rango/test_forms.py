from django.test import TestCase
from rango.models import Society, Event, UserProfile
from django.contrib.auth.models import User
from rango import forms
from django.forms import fields as django_fields
 
class UserTestCase(TestCase):

    def test_user_form(self):
        user_form = forms.UserForm()
        
        fields = user_form.fields
        expected_fields = {'username': django_fields.CharField, 'email': django_fields.EmailField, 'password': django_fields.CharField, 'first_name' : django_fields.CharField, 'last_name' : django_fields.CharField}
        
        for expected_field_name in expected_fields:
            expected_field = expected_fields[expected_field_name]
            self.assertTrue(expected_field_name in fields.keys())
            self.assertEqual(expected_field, type(fields[expected_field_name]))
            
    def test_profile_form(self):
        profile_form = forms.UserProfileForm()
        
        fields = profile_form.fields
        expected_fields = {'picture': django_fields.ImageField}
        
        for expected_field_name in expected_fields:
            expected_field = expected_fields[expected_field_name]
            self.assertTrue(expected_field_name in fields.keys())
            self.assertEqual(expected_field, type(fields[expected_field_name]))
            
class SocietyTestCase(TestCase):

    def test_society_form(self):
        society_form = forms.SocietyForm()
        
        fields = society_form.fields
        expected_fields = {'societyName': django_fields.CharField, 'description': django_fields.CharField, 'logo': django_fields.ImageField}
        
        for expected_field_name in expected_fields:
            expected_field = expected_fields[expected_field_name]
            self.assertTrue(expected_field_name in fields.keys())
            self.assertEqual(expected_field, type(fields[expected_field_name]))
            
class EventTestCase(TestCase):

    def test_event_form(self):
        event_form = forms.EventForm()
        
        fields = event_form.fields
        expected_fields = {'eventName': django_fields.CharField, 'description': django_fields.CharField}
        
        for expected_field_name in expected_fields:
            expected_field = expected_fields[expected_field_name]
            self.assertTrue(expected_field_name in fields.keys())
            self.assertEqual(expected_field, type(fields[expected_field_name]))
""" 
     def test_user_profile_form(self):
       
        user_profile_form = forms.UserProfileForm()
        self.assertEqual(type(user_profile_form.__dict__['instance']), rango.models.UserProfile, f"{FAILURE_HEADER}Your UserProfileForm does not match up to the UserProfile model. Check your Meta definition of UserProfileForm and try again.{FAILURE_FOOTER}")

        fields = user_profile_form.fields

        expected_fields = {
            'picture': django_fields.ImageField,
        }

        for expected_field_name in expected_fields:
            expected_field = expected_fields[expected_field_name]

            self.assertTrue(expected_field_name in fields.keys(), f"{FAILURE_HEADER}The field {expected_field_name} was not found in the UserProfile form. Check you have complied with the specification, and try again.{FAILURE_FOOTER}")
            self.assertEqual(expected_field, type(fields[expected_field_name]), f"{FAILURE_HEADER}The field {expected_field_name} in UserProfileForm was not of the correct type. Expected {expected_field}; got {type(fields[expected_field_name])}.{FAILURE_FOOTER}")
"""