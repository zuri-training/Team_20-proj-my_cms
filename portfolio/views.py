from django.shortcuts import render

# Create your views here.


def portfolio(request):
    return render(request, "portfolio/index.html")

def about(request):
    return render(request, "portfolio/about.html")


def edit(request):
    return render(request, 'base.html')

def contact(request):
    return render(request, "portfolio/contact.html")

def index(request):
    return render(request, "portfolio/index.html")

