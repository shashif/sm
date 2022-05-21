from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from authentication.EmailBackEnd import EmailBackEnd
from django.contrib.auth.decorators import login_required





def homepage(request):
    return render(request, 'hod/homepage.html')
