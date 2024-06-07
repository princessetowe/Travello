from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response


class RegisterAPIVie(APIView):

    def post(self, request, *args, **kwargs):
        first_name = request.data.get['first_name']
        last_name = request.data.get['last_name']
        username = request.data.get['username']
        email = request.data.get['email']
        password1 = request.data.get['password1']
        password2 = request.data.get['password2']
                
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password2, first_name=first_name, last_name=last_name)
                user.save();
                print('Account Created Successfully')
        else:
            print("Passowrd does not match")
            return redirect('/')