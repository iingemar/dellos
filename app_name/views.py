from django.shortcuts import render_to_response
from models import Food


def index(request):
    all_foods = Food.objects.prefetch_related('ingredients').all().order_by('index')
    pizzas = all_foods.filter(category__name='Pizza')
    pastas = all_foods.filter(category__name='Pasta')
    context = {
        'pizzas': pizzas,
        'pastas': pastas
    }

    return render_to_response('index.html', context)