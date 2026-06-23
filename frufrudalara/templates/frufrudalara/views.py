from django.shortcuts import render

def sobre(request):
    return render(request, "frufrudalara/sobre.html")

def login(request):
    return render(request, "frufrudalara/login.html")

def produtos(request):
    return render(request, "frufrudalara/produtos.html")