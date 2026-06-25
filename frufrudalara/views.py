from django.shortcuts import render

def sobre(request):
    return render(request, "frufrudalara/tela1.html")

def login(request):
    return render(request, "frufrudalara/tela2.html")

def produtos(request):
    return render(request, "frufrudalara/tela3.html")

