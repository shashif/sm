from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.




def authregistration(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username already exists!')
                
            elif  User.objects.filter(email=email).exists():  
                messages.error(request, 'Email id  already exists!') 
                
            else: user=User.objects.create_user(username=username, password=password,
                                email=email)
            user.save()
            return redirect('login')
                
        else:    
            messages.error(request, 'Your password is not matched!')
            

    return render(request, 'authentication/registration.html')


def authforgotpassword(request):
    return render(request, 'authentication/forgotpassword.html')


def authlogout(request):
    logout(request)
    messages.success(
        request, 'logged out')
    return redirect('home')


# messages.error(request, 'Your password is not matched!')


# if User.objects.filter(username=username).exists():
#                     messages.error(
#                     request, 'username already exists')

#                 elif User.objects.filter(email=email).exists():
