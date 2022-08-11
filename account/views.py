from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm

# # Create your views here.
def signin(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
           login(request, user)
           return redirect ('/')
        else:
            print("user does not exist, did you forget your password?")
            
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def templates(request):
    return render(request, 'template.html')

def contact(request):
    return render(request, 'contact-us.html')

