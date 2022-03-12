from django.shortcuts import render
from rango.models import Society, Event
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    context_dict = {}

    return render(request, 'Clubs&Socs/index.html', context_dict)

def societies(request):
    context_dict = {}

    return render(request, 'Clubs&Socs/societies.html', context_dict)

#add html    
def society(request):
    context_dict = {}

    return render(request, 'Clubs&Socs/society.html', context_dict)

#add html    
def event(request):
    context_dict = {}

    return render(request, 'Clubs&Socs/event.html', context_dict)
    
def show_society(request, society_name_slug):
    context_dict = {}
    
    try: 
        society = Society.objects.get(slug = society_name_slug)
        
        events = Event.objects.filter(societyName = society)
        context_dict ['events'] = events
        context_dict['society'] = society
        
    except Society.DoesNotExist:
        context_dict ['events'] = None
        context_dict['society'] = None
    
    return render(request, 'Clubs&Socs/societies.html', context=context_dict)
    
    
# Figure out how to create show_event
def show_event(request, event_name_slug):
    context_dict = {}
    
    try: 
        event = Event.objects.get(slug = event_name_slug)
        context_dict ['event'] = event
        
    except Society.DoesNotExist:
        context_dict ['event'] = None
    
    return render(request, 'Clubs&Socs/event.html', context=context_dict)


def discover(request):
    context_dict = {}

    return render(request, 'Clubs&Socs/discover.html', context_dict)

def result(request):
    context_dict = {}

    return render(request, 'Clubs&Socs/result.html', context_dict)

def wellbeing(request):
    context_dict = {}

    return render(request, 'Clubs&Socs/wellbeing.html', context_dict)

def howto(request):
    context_dict = {}

    return render(request, 'Clubs&Socs/how-to.html', context_dict)

def myaccount(request):
    context_dict = {}

    return render(request, 'Clubs&Socs/my-account.html', context_dict)

#We may need two separate login views for society and regular user?
def login(request):
    context_dict = {}

    return render(request, 'Clubs&Socs/login.html', context_dict)
    
@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('Clubs&Socs:index'))

def register(request):
    context_dict = {}

    return render(request, 'Clubs&Socs/register.html', context_dict)


def signup(request):
    context_dict = {}

    return render(request, 'Clubs&Socs/sign-up.html', context_dict)
