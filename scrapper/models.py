from django.db import models

# Create your models here.
class Scrape(models.Model):
    site        = models.CharField(max_length=50)
    keyword     = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.site} - {self.keyword}'


class Result(models.Model):
    Scrape      = models.ForeignKey(Scrape, on_delete=models.CASCADE)

    date        = models.DateTimeField()
    contents    = models.TextField(blank=True)
    matches     = models.IntegerField(blank=True)

    def __str__(self):
        return f'{self.date} - {self.matches}'