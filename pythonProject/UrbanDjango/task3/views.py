from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'third_task/index.html')


def games(request):
    games = ["Atomic Heart", "Cyberpunk 2077", "Payday 2"]
    context = {
        "games": games
    }
    return render(request, 'third_task/games.html', context)


def cart(request):
    return render(request, 'third_task/cart.html')