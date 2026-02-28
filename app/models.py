from django.db import models
from django.http import HttpRequest
from django.shortcuts import render
# Create your models here.
def home(request):
    return render(request,'home.html')