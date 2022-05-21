
from django.urls import path
from .import views

urlpatterns = [

    
    path('registration/', views.authregistration,name='registration'),
    path('forgot-password/', views.authforgotpassword,name='forgotpassword'),
    path('logout', views.authlogout,name='logout'),

]
