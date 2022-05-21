from http.client import HTTPResponse
from multiprocessing import context
from tkinter.messagebox import NO
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from authentication.EmailBackEnd import EmailBackEnd
from authentication.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt



def home(request):
    if request.method != "POST":
        return render(request, 'index.html')

    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'),
                                         password=request.POST.get('password'))
    if user != None:
        login(request, user)
        user_type = user.user_type
        # return HttpResponse("Email: "+request.POST.get('email')+ " Password: "+request.POST.get('password'))
        if user_type == '1':
            #    return render(request, 'homepage.html')
            return redirect('homepage')

        elif user_type == '2':
            # return HttpResponse("Staff Login")
            return redirect('staff_home')

        elif user_type == '3':
            # return HttpResponse("Student Login")
            return redirect('student_home')

        elif user_type == '4':
            # return HttpResponse("Student Login")
            return redirect('teacher_home')
        else:
            messages.error(request, "Invalid Login!")
            return render(request, 'index.html')

    else:
        messages.error(request, "Invalid Login Credentials!")
        # return HttpResponseRedirect("/")
        return render(request, 'index.html')


def get_user_details(request):
    if request.user != None:
        return HttpResponse("User: " + request.user.email + " User Type: " + request.user.user_type)
    else:
        return HttpResponse("Please Login First")




def profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    context = {
        "user": user,
    }
    return render(request, 'profile.html', context)


def profile_update(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        # email=request.POST.get('email')
        # username=request.POST.get('username')

        password = request.POST.get('password')

        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name

            
            
            # pbkdf2_sha256$320000$yQsZcg79ubqG2WGjS77go5$TDxbxbXhgJ6/wwD3FeBSurVZX7MS3QU8/Ddp2aefxoM=
                
            if profile_pic is not None and profile_pic != "":
                customuser.profile_pic = profile_pic

            if password != None and password != "":
                customuser.set_password(password)
            
            
            customuser.save()
            messages.success(request, 'Updated')
            return redirect('profile')

        except:
            messages.error(request, 'Not Updated')
    return render(request, 'profile.html')

# def homepage(request):
#     return render(request, 'homepage.html')
