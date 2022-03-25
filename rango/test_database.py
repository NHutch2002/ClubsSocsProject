from django.test import TestCase
from rango.models import Society, Event, UserProfile
from django.contrib.auth.models import User
import datetime

class SocietyTestCase(TestCase):
    def setUp(self):
        Society.objects.create(societyName = 'Sport', description = 'The sports society', views = 1464, memberNum = 124)
        Society.objects.create(societyName = 'Art', description = 'The art society', views = 1162, memberNum = 64)
        
    def test_society_creation(self):
        sport = Society.objects.get(societyName = 'Sport')
        art = Society.objects.get(societyName = 'Art')
        self.assertEqual(sport.slug, 'sport')
        self.assertEqual(sport.description, 'The sports society')
        self.assertEqual(sport.views, 1464)
        self.assertEqual(sport.memberNum, 124)
        self.assertEqual(art.slug, 'art')
        self.assertEqual(art.description, 'The art society')
        self.assertEqual(art.views, 1162)
        self.assertEqual(art.memberNum, 64)

class EventTestCase(TestCase):
    def setUp(self):
        Society.objects.create(societyName = 'Sport', description = 'The sports society', views = 1464, memberNum = 124)
        Society.objects.create(societyName = 'Art', description = 'The art society', views = 1162, memberNum = 64)
        Event.objects.create(society = Society.objects.get(societyName = 'Art'), eventName = 'Painting workshop', description = 'Learn to paint from Rob Boss', memberNum = 10, date = datetime.datetime(2022,7,2))
        Event.objects.create(society = Society.objects.get(societyName = 'Sport'), eventName = 'Charity basketball', description = 'Exhibition basketball tournament, all proceeds to charity', memberNum = 17, date = datetime.datetime (2022,4,3))
        
    def test_event_creation(self):
        paint = Event.objects.get(eventName = 'Painting workshop')
        basketball = Event.objects.get(eventName = 'Charity basketball')
        self.assertEqual(paint.slug, 'painting-workshop')
        self.assertEqual(paint.description, 'Learn to paint from Rob Boss')
        self.assertEqual(paint.date, datetime.date(2022,7,2))
        self.assertEqual(paint.memberNum, 10)
        self.assertEqual(basketball.slug, 'charity-basketball')
        self.assertEqual(basketball.description, 'Exhibition basketball tournament, all proceeds to charity')
        self.assertEqual(basketball.date, datetime.date(2022,4,3))
        self.assertEqual(basketball.memberNum, 17)      

class UserTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username='username', first_name='User', last_name='Name', email='user@name.com')
        user.set_password('password')
        user.save()
        profile = UserProfile.objects.create(user = user, is_student = True)

    def test_user_creation(self):
        user = User.objects.get(username = 'username')
        profile = UserProfile.objects.get(user = user)
        self.assertEqual(profile.is_student, True)
        self.assertEqual(profile.is_society, False)