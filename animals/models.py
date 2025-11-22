from django.db import models

class Animal(models.Model):
    aid = models.CharField(primary_key=True, max_length=20)
    title = models.CharField(max_length=100, null=True, blank=True)
    image = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    food = models.CharField(max_length=50, null=True, blank=True)
    place = models.CharField(max_length=100, null=True, blank=True)
    donated_by = models.CharField(max_length=100, null=True, blank=True)
    care_taker = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title if self.title else "Animal"


