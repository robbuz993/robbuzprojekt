from django.forms import ModelForm
from .models import film

class FilmForm(ModelForm):
    class Meta:
        model = film
        fields = ['tytul', 'opis', 'premiera', 'rok', 'imdb_rating', 'plakat']