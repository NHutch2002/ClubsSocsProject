import datetime
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ClubsSocsProject.settings')

import django
django.setup()
from rango.models import Society, Event, UserProfile
from django.contrib.auth.models import User

def populate():
        
    sport_events = [
        {'eventName' : '5-a-side football', 'description' : 'A fun friendly fives game of kicking a round object', 'memberNum' : 10, 'date' : datetime.datetime(2022,2,2)},
        {'eventName' : 'Charity basketball', 'description' : 'Exhibition basketball tournament, all proceeds to charity', 'memberNum' : 17, 'date' : datetime.datetime (2022,4,3)},
        {'eventName' : 'Yoga', 'description' : 'Weekly yoga session', 'memberNum' : 4, 'date' : datetime.datetime(2022,3,7)}
    ]
    
    art_events = [
        {'eventName' : 'Painting workshop', 'description' : 'Learn to paint from Rob Boss', 'memberNum' : 10, 'date' : datetime.datetime(2022,7,2)},
        {'eventName' : 'Karaoke', 'description' : 'You know what karaoke is', 'memberNum' : 7, 'date' : datetime.datetime (2022,4,12)},
        {'eventName' : 'Slam poetry night', 'description' : 'Weekly slam poetry session', 'memberNum' : 4, 'date' : datetime.datetime(2022,3,7)}
    ]
    
    sport_society = {'societyName' : 'Sport', 'events': sport_events, 'description': 'The sports society', 'views': 1464, 'memberNum' : 124}
    art_society = {'societyName' : 'Art','events': art_events, 'description': 'The sports society', 'views': 1162, 'memberNum' : 64}
    
    users = {'Student1': {'firstname' : 'student', 'lastname' : '1', 'email' : 'student1@gmail.com', 'password' : 'WaD2-2021', 'is_student' : True, 'is_society' : False, 'member' : ['Sport'], 'event' : ['Yoga']},
            'Student2' : {'firstname' : 'student', 'lastname' : '2', 'email' : 'student2@gmail.com', 'password' : 'WaD2-2021', 'is_student' : True, 'is_society' : False, 'member' : ['Art', 'Sport'], 'event' : ['5-a-side football','Karaoke']},
            'Society1' : {'society' : sport_society, 'firstname' : 'society', 'lastname' : '1', 'email' : 'society1@gmail.com', 'password' : 'WaD2-2021', 'is_student' : False, 'is_society' : True},
            'Society2': {'society' : art_society, 'firstname' : 'society', 'lastname' : '2', 'email' : 'society2@gmail.com', 'password' : 'WaD2-2021', 'is_student' : False, 'is_society' : True}}

    for user, user_data in users.items():
        u = add_user(user, user_data['firstname'], user_data['lastname'], user_data['email'], user_data['password'], user_data['is_student'], user_data['is_society'])
        if (user_data['is_society'] == True):
            soc = user_data['society']
            s = add_soc(u, soc['societyName'], soc['description'], soc['views'], soc['memberNum'])
            for e in soc['events']:
                add_event(s, e['eventName'], e['description'], e['date'], e['memberNum'])
                
    for username, user_data in users.items():
        if (user_data['is_society'] == False):
            for societyName in user_data['member']:
                s = Society.objects.get(societyName = societyName)
                user = User.objects.get(username = username)
                profile = UserProfile.objects.get(user = user)
                s.member.add(profile)
                s.save()
            for eventName in user_data['event']:
                e = Event.objects.get(eventName = eventName)
                user = User.objects.get(username = username)
                profile = UserProfile.objects.get(user = user)
                e.attendee.add(profile)
                e.save()
    
    for s in Society.objects.all():
        for e in Event.objects.filter(society=s):
            print(f'- {s}: {e}')

def add_event(soc, eventName, description, date, memberNum=0):
    e = Event.objects.get_or_create(society=soc, eventName=eventName)[0]
    e.description=description
    e.memberNum=memberNum
    e.date=date
    e.save()
    return e

def add_soc(owner, societyName, description, views=0, memberNum=0):
    s = Society.objects.get_or_create(owner = owner, societyName=societyName)[0]
    s.description = description
    s.views = views
    s.memberNum = memberNum
    s.save()
    return s
    
def add_user(username, firstname, lastname, email, password, is_student, is_society):
    new_user = User.objects.get_or_create(username = username, first_name = firstname, last_name = lastname, email = email, password = password)[0]
    new_user.set_password(new_user.password)
    new_user.save()
    u = UserProfile.objects.get_or_create(user = new_user)[0]
    u.is_student = is_student
    u.is_society = is_society
    u.save()
    return u

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()