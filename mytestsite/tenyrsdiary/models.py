from django.db import models
import datetime

# Create your models here.
class Diary(models.Model):
    diary_date = models.DateField(unique=True, primary_key=True)

class TodoList(models.Model):
    date = models.ForeignKey(Diary, on_delete=models.CASCADE)
    todo_text = models.CharField(max_length=100)
    todo_check = models.BooleanField(default=False)

class Asset(models.Model):
    date = models.ForeignKey(Diary, on_delete=models.CASCADE)
    content = models.TextField(blank=True)

class Family(models.Model):
    date = models.ForeignKey(Diary, on_delete=models.CASCADE)
    content = models.TextField(blank=True)

class Suprise(models.Model):
    date = models.ForeignKey(Diary, on_delete=models.CASCADE)
    content = models.TextField(blank=True)

class Relationship(models.Model):
    date = models.ForeignKey(Diary, on_delete=models.CASCADE)
    content = models.TextField(blank=True)

class Study(models.Model):
    date = models.ForeignKey(Diary, on_delete=models.CASCADE)
    content = models.TextField(blank=True)

class Career(models.Model):
    date = models.ForeignKey(Diary, on_delete=models.CASCADE)
    content = models.TextField(blank=True)

class Mind(models.Model):
    date = models.ForeignKey(Diary, on_delete=models.CASCADE)
    content = models.TextField(blank=True)