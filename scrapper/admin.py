from django.contrib import admin

# Register your models here.
from scrapper.models import Scrape, Results

class ScrapeAdmin(admin.ModelAdmin):
    pass

class ResultsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Scrape, ScrapeAdmin)
admin.site.register(Results, ResultsAdmin)