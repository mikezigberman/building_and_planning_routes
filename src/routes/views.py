from django.contrib import messages
from django.shortcuts import render
from routes.forms import RouteForm

def home(request):
    form = RouteForm()
    return render(request, 'routes/home.html', {'form': form})

def find_routes(request):
    if request.method == "POST":
        form = RouteForm(request.POST)
        return render(request, 'routes/home.html', {'form': form})
    else:
        form = RouteForm()
        messages.error(request, "No data to search")
        return render(request, 'routes/home.html', {'form': form})
