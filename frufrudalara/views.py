from django.shortcuts import render

def sobre(request):
    return render(request, "frufrudalara/tela1.html")

def login(request):
    return render(request, "frufrudalara/tela2.html")

def produtos(request):
    
    itens = [
        {
            "id": 1,
            "imagem": 'img/image 2.png',
        
        },
        {
            "id": 2,
            "imagem": 'img/image 3.png',
        
        },
        {
            "id": 3,
            "imagem": 'img/image 4.png',
            
        },
        {
            "id": 4,
            "imagem": 'img/image 5.png',
            
        },
    ]

    context = {
        "itens": itens,
    }
    return render(request, "frufrudalara/tela3.html")

