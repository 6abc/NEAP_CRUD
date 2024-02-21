from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    director = models.CharField(max_length=120)
    poster = models.ImageField(upload_to='images/')
    plot = models.TextField()
    def __str__(self):
        return self.title