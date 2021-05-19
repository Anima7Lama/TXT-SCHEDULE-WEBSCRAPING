from django.db import models

# Create your models here.
class ScrapedData(models.Model):
    date = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    time = models.DateTimeField()
    task = models.CharField(max_length=500)

    def __str__(self):
        return self.task