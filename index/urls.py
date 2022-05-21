
from django.urls import path
from .import views,HodViews

urlpatterns = [

    path('', views.home,name='home'),
    
    
    
    # URSL for HOD
    path('homepage', HodViews.homepage,name='homepage'),
    
    #profile update
    path('profile', views.profile,name='profile'),
    path('profile/update', views.profile_update,name='profile_update'),
    
    
    # URSL for Student
    
    
     # URLS for Staff

]
