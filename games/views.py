from django.shortcuts import render

from .models import Game

def homepage(request):
    games = Game.objects
    return render(request, 'games/home.html',{'games':games})
