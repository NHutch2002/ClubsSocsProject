from django.shortcuts import render


def index(request):
    context_dict = {}

    return render(request, 'rango/index.html', context_dict)

def societies(request):
    context_dict = {}

    return render(request, 'rango/societies.html', context_dict)

def discover(request):
    context_dict = {}

    return render(request, 'rango/discover.html', context_dict)

def result(request):
    context_dict = {}

    return render(request, 'rango/result.html', context_dict)

def wellbeing(request):
    context_dict = {}

    return render(request, 'rango/wellbeing.html', context_dict)

def howto(request):
    context_dict = {}

    return render(request, 'rango/how-to.html', context_dict)

def myaccount(request):
    context_dict = {}

    return render(request, 'rango/my-account.html', context_dict)

def login(request):
    context_dict = {}

    return render(request, 'rango/login.html', context_dict)

def register(request):
    context_dict = {}

    return render(request, 'rango/register.html', context_dict)


def signup(request):
    context_dict = {}

    return render(request, 'rango/sign-up.html', context_dict)
