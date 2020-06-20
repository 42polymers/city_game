from django.shortcuts import render

from .forms import WorldBorderForm


def index(request):
    form = WorldBorderForm()
    context = {'form': form}
    return render(request, 'index.html', context)
