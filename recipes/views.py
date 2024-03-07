from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Pedro Dias Toledo',
    })

def sobre(request):
    return HttpResponse('Um Lindo Dia')

def receita(request):
    return HttpResponse('Receita')

def contato(request):
    return render(request, 'me_apague/temp.html')