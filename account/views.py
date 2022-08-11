from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from multiprocessing import context
from account.forms import RegistrationForm


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


def register_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, user, account)
            return redirect('home')
        else:
            context['registration_form'] = form

    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'account/register1.html', context)



 
def home(request):
    return render(request,"home1.html")  



# class SignUp(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "register.html"
# =======
def templates(request):
    return render(request, 'template.html')


