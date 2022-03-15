from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test
from rango.models import UserProfile

def is_student(user):
    profile = UserProfile.objects.get(user = user)
    return user.is_active and profile.is_student


def student_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='Clubs&Socs:index'):

    concrete_decorator = user_passes_test(
        lambda user: user.is_active and is_student(user),
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return concrete_decorator(function)
    return concrete_decorator

def is_society(user):
    profile = UserProfile.objects.get(user = user)
    return user.is_active and profile.is_society

def society_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='Clubs&Socs:index'):

    concrete_decorator = user_passes_test(
        lambda user: user.is_active and is_society(user),
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return concrete_decorator(function)
    return concrete_decorator