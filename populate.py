import datetime
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ClubsSocsProject.settings')

import django
django.setup()
from rango.models import Society, Event

def populate():
        
    sport_events = [
        {'eventName' : '5-a-side football', 'description' : 'A fun friendly fives game of kicking a round object', 'members' : 10, 'date' : datetime.datetime(2022,2,2)},
        {'eventName' : 'Charity basketball', 'description' : 'Exhibition basketball tournament, all proceeds to charity', 'members' : 17, 'date' : datetime.datetime (2022,4,3)},
        {'eventName' : 'Yoga', 'description' : 'Weekly yoga session', 'members' : 4, 'date' : datetime.datetime(2022,3,7)}
    ]

    socs = {'Sport': {'events': sport_events, 'description': 'The sports society', 'views': 1464, 'members' : 124}}

    for soc, soc_data in socs.items():
        s = add_soc(soc, soc_data['description'], soc_data['views'], soc_data['members'])
        for e in soc_data['events']:
            add_event(s, e['eventName'], e['description'], e['date'], e['members'])

    for s in Society.objects.all():
        for e in Event.objects.filter(societyName=s):
            print(f'- {s}: {e}')

def add_event(soc, eventName, description, date, members=0):
    e = Event.objects.get_or_create(societyName=soc, eventName=eventName)[0]
    e.description=description
    e.members=members
    e.date=date
    e.save()
    return e

def add_soc(societyName, description, views=0, members=0):
    s = Society.objects.get_or_create(societyName=societyName)[0]
    s.description = description
    s.views = views
    s.members = members
    s.save()
    return s

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()