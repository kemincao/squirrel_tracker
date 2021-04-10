from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from sightings.models import Squirrels

def map(request):
    squirrels = Squirrels.objects.all()[:100]
    context = {'squirrels': squirrels}

    return render(request, 'map/map.html', context)
# Create your views here.
