from django.db import models

# Create your models here.
class Diary(models.Model):
    today = models.DateTimeField()
    birth = models.CharField(max_length=100)
    weather = models.CharField(max_length=100)
    #7個主題
    mind = models.TextField(blank=True)
    career = models.TextField(blank=True)
    study = models.TextField(blank=True)
    relationship = models.TextField(blank=True)
    asset = models.TextField(blank=True)
    family = models.TextField(blank=True)
    suprise = models.TextField(blank=True)
    #todo清單
    todo = models.CharField(max_length=100)
    todo_check = models.BooleanField(default=False)
    