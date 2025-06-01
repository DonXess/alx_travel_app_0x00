from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    # A very simple HTML response
    return HttpResponse('<h1>Welcome to ALX Travel App!</h1><p>Your project is running.</p>')