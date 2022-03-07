from django.urls import path
from rango import views

app_name = 'Clubs&Socs'

urlpatterns = [
    path('', views.index, name='index'),
    path('societies/', views.societies, name='societies'),
    #Check two lines below to ensure they are correct url mapping for parameterized url
    path('societies/<slug:society_name_slug>/', views.show_society, name='show_society'),
    path('societies/<slug:society_name_slug>/<slug:event_name_slug>/', views.show_event, name='show_event'),
    path('discover/', views.discover, name='discover'),
    path('result/', views.result, name='result'),
    path('wellbeing/', views.wellbeing, name='wellbeing'),
    path('how-to/', views.howto, name='howto'),
    path('my-account/', views.myaccount, name='myaccount'),
    path('login/', views.login, name='login'),
    path('login/register/', views.register, name='register'),
    path('login/sign-up/', views.signup, name='signup'),
]
