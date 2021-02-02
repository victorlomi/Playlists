from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("welcome to the lists app")

def signup(request):
    pass
