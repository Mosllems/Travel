from django.urls import path
from . import views

app_name = 'website' # we must write the apps'name here, because once the project get bigger calling the urls will be harder, and by app name we can distinguish them from eachother


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),

]
