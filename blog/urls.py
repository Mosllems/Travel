from django.urls import path
from . import views

app_name = 'blog' # we must write the apps'name here, because once the project get bigger calling the urls will be harder, and by app name we can distinguish them from eachother


urlpatterns = [
    path('', views.blogview, name='blogview'),
    path('detail/', views.blogdetail, name='blogdetail'),

]
