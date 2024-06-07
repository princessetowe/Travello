from django.shortcuts import render
from .models import Destination
# Create your views here.
dests = Destination.objects.all()

def index(request):
    return render(request, 'index.html', {'dests': dests})

def about(request):
    return render(request, 'about.html', {'dests': dests})

def destinations(request):
    return render(request, 'destinations.html', {'dests': dests})

def contact(request):
    return render(request, 'contact.html', {'dests': dests})

def news(request):
    return render(request, 'news.html', {'dests': dests})