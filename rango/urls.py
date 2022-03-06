from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    path('societies/', views.societies, name='societies'),
    path('discover/', views.discover, name='discover'),
    path('result/', views.result, name='result'),
    path('wellbeing/', views.wellbeing, name='wellbeing'),
    path('how-to/', views.howto, name='howto'),
]
