from django.shortcuts import render_to_response
from django.shortcuts import render
from models import Food


def index(request):
    foods = Food.objects.filter(category__name='Pizza').prefetch_related('ingredients').all().order_by('index')
    context = {
        'foods': foods
    }

    return render_to_response('index.html', context)