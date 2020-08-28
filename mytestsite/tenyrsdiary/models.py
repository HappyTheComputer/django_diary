from django.db import models
import datetime

# Create your models here.
class DayInYesr(models.Model):
    dayKey = models.CharField("日期", max_length=10, unique=True, primary_key=True)

class Diary(models.Model):
    diary_date = models.DateField(unique=True, primary_key=True)
    dayKey = models.ForeignKey(DayInYesr, on_delete=models.CASCADE)

    def day(self):
        return diary_date.date().strftime("%m-%d")
    
    def year(self):
        return diary_date.date().strftime("%Y")
        
class BirthDay(models.Model):
    dayKey = models.ForeignKey(DayInYesr, on_delete=models.CASCADE)
    birthName = models.CharField("壽星", max_length=30)

class MemorialDay(models.Model):
    dayKey = models.ForeignKey(DayInYesr, on_delete=models.CASCADE)
    event = models.CharField("紀念日", max_length=100)

class TodoList(models.Model):
    date = models.ForeignKey(Diary, on_delete=models.CASCADE)
    todo_text = models.CharField(max_length=100)
    todo_check = models.BooleanField(default=False)

    def __str__(self):
        return self.todo_text

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