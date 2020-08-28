from django.contrib import admin
from .models import DayInYesr, Diary, TodoList, BirthDay, MemorialDay, Asset, Family, Suprise, Relationship, Study, Career, Mind

# Register your models here.
class BirthInline(admin.TabularInline):
    model = BirthDay
    extra = 1

class MemorialInline(admin.TabularInline):
    model = MemorialDay
    extra = 1

class DairyYrInline(admin.TabularInline):
    model = Diary
    extra = 1

class DayAdmin(admin.ModelAdmin):
    inlines = [BirthInline, MemorialInline, DairyYrInline] 

admin.site.register(DayInYesr, DayAdmin)
admin.site.register(Diary)