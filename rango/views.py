from django.shortcuts import render


def index(request):
    context_dict = {}

    return render(request, 'Clubs&Socs/index.html', context_dict)

def societies(request):
    context_dict = {}

    return render(request, 'Clubs&Socs/societies.html', context_dict)

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

def login(request):
    context_dict = {}

    return render(request, 'Clubs&Socs/login.html', context_dict)

def register(request):
    context_dict = {}

    return render(request, 'Clubs&Socs/register.html', context_dict)


def signup(request):
    context_dict = {}

    return render(request, 'Clubs&Socs/sign-up.html', context_dict)
