from django.shortcuts import render
from django.http import HttpResponse
from .views import *
from .models import *
# Create your views here.

def restro(request):
    return render(request)
