from django.contrib import admin

# Register your models here.
from scrapper.models import Scrape, Result

class ScrapeAdmin(admin.ModelAdmin):
    pass

class ResultsAdmin(admin.ModelAdmin):
    list_display =  ('Scrape', 'date', 'matches')

admin.site.register(Scrape, ScrapeAdmin)
admin.site.register(Result, ResultsAdmin)