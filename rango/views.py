from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from rango.models import Society, Event, UserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rango.forms import SocietyForm, UserForm, UserProfileForm, EventForm
from rango.decorators import society_required, student_required
from django.views import View


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
        events = Event.objects.filter(society = society)
        context_dict ['events'] = events
        context_dict['society'] = society
        
        current_user =  request.user
        current_profile = UserProfile.objects.get(user=current_user)
        context_dict['user_profile'] = current_profile


    except:
        society = None
    
    if society is None:
        return redirect(reverse('Clubs&Socs:index'))
    
    return render(request, 'Clubs&Socs/society.html', context=context_dict)
    
    
# Figure out how to create show_event
def show_event(request, society_name_slug, event_name_slug):
    context_dict = {}
    
    try:
        society = Society.objects.get(slug = society_name_slug) 
        event = Event.objects.get(slug = event_name_slug)
        context_dict ['society'] = society
        context_dict ['event'] = event

        current_user =  request.user
        current_profile = UserProfile.objects.get(user=current_user)
        context_dict['user_profile'] = current_profile
        
    except:
        event = None
    
    if event is None:
        return redirect(reverse('Clubs&Socs:index'))
    
    return render(request, 'Clubs&Socs/event.html', context=context_dict)
    
@login_required
@society_required
def add_event(request):
    try:
        current_user = request.user
        current_profile = UserProfile.objects.get(user=current_user)
        society = Society.objects.get(owner=current_profile)
    except:
        society = None
    
    if society is None:
        return redirect(reverse('Clubs&Socs:index'))

    form = EventForm()

    if request.method == 'POST':
        form = EventForm(request.POST)

        if form.is_valid():
            if society:
                event = form.save(commit=False)
                event.society = society
                event.memberNum = 0
                event.save()

                return redirect(reverse('Clubs&Socs:myaccount'))
        else:
            print(form.errors)
    
    context_dict = {'form': form}
    return render(request, 'Clubs&Socs/add-event.html', context=context_dict)


@login_required
@student_required
def discover(request):
    event_list = Event.objects.order_by('-date')[:3]
    print(event_list)
    context_dict = {}
    context_dict['events'] = event_list
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

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('Clubs&Socs:index'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'Clubs&Socs/login.html')
    
@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('Clubs&Socs:index'))

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        society_form = SocietyForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid() and society_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.is_society = True
            profile.is_student = False
            
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                
            profile.save()
            
            society = society_form.save(commit=False)
            society.owner = profile

            if 'logo' in request.FILES:
                society.logo = request.FILES['logo']
            
            society.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors, society_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        society_form = SocietyForm()
    
    return render(request, 'Clubs&Socs/register.html', context={'user_form': user_form, 'profile_form': profile_form, 'society_form': society_form, 'registered': registered})


def signup(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.is_society = False
            profile.is_student = True
            
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
                
            profile.save()
            
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request, 'Clubs&Socs/signup.html', context={'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

#@login_required
#@student_required
class JoinButtonView(View):
    def get(self, request):
        society_id = request.GET['society_id']
        society = Society.objects.get(societyName = society_id)
        current_user =  request.user
        current_profile = UserProfile.objects.get(user=current_user)
        society.member.add(current_profile)
        society.memberNum = society.memberNum + 1
        society.save()

        return HttpResponse()

class EventButtonView(View):
    def get(self, request):
        event_name = request.GET['event_name']
        event = Event.objects.get(eventName = event_name)
        current_user =  request.user
        current_profile = UserProfile.objects.get(user=current_user)
        event.attendee.add(current_profile)
        event.memberNum = event.memberNum + 1
        event.save()

        return HttpResponse()


