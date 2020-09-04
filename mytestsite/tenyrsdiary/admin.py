from django.contrib import admin
from .models import Diary, TodoList, Asset, Family, Suprise, Relationship, Study, Career, Mind

# Register your models here.
class TodoListInline(admin.TabularInline):
    model = TodoList
    extra = 1

class AssetInline(admin.TabularInline):
    model = Asset
    extra = 1

class FamilyInline(admin.TabularInline):
    model = Family
    extra = 1

class SupriseInline(admin.TabularInline):
    model = Suprise
    extra = 1

class RelationshipInline(admin.TabularInline):
    model = Relationship
    extra = 1

class StudyInline(admin.TabularInline):
    model = Study
    extra = 1

class CareerInline(admin.TabularInline):
    model = Career
    extra = 1

class MindInline(admin.TabularInline):
    model = Mind
    extra = 1

class DairyAdmin(admin.ModelAdmin): 
    inlines = [TodoListInline, AssetInline, FamilyInline, RelationshipInline, StudyInline, CareerInline, MindInline, SupriseInline]

admin.site.register(Diary, DairyAdmin)