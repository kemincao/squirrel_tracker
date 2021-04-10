from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Squirrels
from .forms import SquirrelForm

def index(request):
    squirrels = Squirrels.objects.all()
    context = {
        'squirrels': squirrels
    }
    return render(request, 'sightings/index.html', context)

def details(request, Unique_squirrel_id):
    squirrel = Squirrels.objects.get(id=Unique_squirrel_id)
    context={
        "squirrel": squirrel,
    }
    return render(request, 'sightings/details.html', context)

def update(request, Unique_squirrel_id):
    if not request:
        return Http404('Page Not Found')
    if request.method=="POST":
        form = SquirrelForm(request.POST, instance=Squirrels)
        if form.is_valid():
            form.save()
            squirrel = Squirrels.objects.get(id=Unique_squirrel_id)
            context={
                "squirrel": squirrel,
            }
            return redirect('sightings/details.html',context)
    else:
        form = SquirrelForm(instance = Squirrels)
    context = {'form': form}
    return render(request, 'sightings/update.html', context)

def add(request):
    if request.method=="POST":
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            squirrel = Squirrels.objects.get(id=Unique_squirrel_id)
            context={
                "squirrel": squirrel,
            }
            return redirect('sightings/details.html',context)
    else:
        form = SquirrelForm()
    context = {'form': form}
    return render(request, 'sightings/update.html', context)

def stats(request):
    squirrel_stat1 = Squirrels.objects.all().count()
    squirrel_stat2 = Squirrels.objects.filter(Fur = "Cinnamon").count()
    squirrel_stat3 = Squirrels.objects.filter(Age = "Adult").count()
    squirrel_stat4 = Squirrels.objects.filter(Location = "Ground Plane").count()
    squirrel_stat5 = Squirrels.objects.filter(Eating = "True").count()
    context = {
        "Fact1": squirrel_stat1,
        "Fact2": squirrel_stat2,
        "Fact3": squirrel_stat3,
        "Fact4": squirrel_stat4,
        "Fact5": squirrel_stat5,
        }
    return render(request, 'sightings/stats.html', context)
