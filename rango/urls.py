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
    path('my-account/add-event', views.add_event, name='add_event'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'), #society registration
    path('signup/', views.signup, name='signup'), #user sign-up
    path('logout/', views.user_logout, name='logout'),
]
