from django.contrib import admin
from .models import film

#admin.site.register(film)
@admin.register(film)
class filmAdmin(admin.ModelAdmin):
    #fields = ["tytul", "opis", "rok"]
    #exclude = ["opis"]  - czyli moge cos wykluczyc
    list_display = ["tytul", "imdb_rating", "rok"]
    list_filter = ("rok", "imdb_rating")
    search_fields = ("tytul", "opis")