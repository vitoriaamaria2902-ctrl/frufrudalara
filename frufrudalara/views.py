from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def sobre (request):
    return HttpResponse("sobre")

def login(request):
    return HttpResponse("login")

def produtos(request):
    return HttpResponse("produtos")