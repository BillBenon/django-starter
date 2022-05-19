from django.contrib import admin

# Register your models here.
from . import models


class MovieAdmin(admin.ModelAdmin):
    fields = ['release_year', 'title', 'length']

    search_fields = ['title', 'length']


admin.site.register(models.Customer)
admin.site.register(models.Movie, MovieAdmin)
