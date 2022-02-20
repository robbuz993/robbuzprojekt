from django.shortcuts import render, get_object_or_404, redirect
from .models import film
from .forms import FilmForm
from django.contrib.auth.decorators import login_required


@login_required
def wszystkie_filmy(request):
    wszystkie = film.objects.all()
    return render(request, 'filmy.html', {'filmy': wszystkie})

def nowy_film(request):
    form = FilmForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        form.save()
        return redirect(wszystkie_filmy)

    return render(request, 'film_form.html', {'form': form, 'nowy': True})

def edytuj_film(request, id):
    Film = get_object_or_404(film, pk=id)
    form = FilmForm(request.POST or None, request.FILES or None, instance=Film)
    
    if form.is_valid():
        form.save()
        return redirect(wszystkie_filmy)

    return render(request, 'film_form.html', {'form': form, 'nowy': False})

def usun_film(request, id):
    Film = get_object_or_404(film, pk=id)
    
    if request.method == "POST":
        Film.delete()
        return redirect(wszystkie_filmy)

    return render(request, 'potwierdz.html', {'film': Film})