from django.contrib import admin

from randomizer.models import Category, Word, WordCategory   # use the correct import for your models


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    ordering = ['name']


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_filter = ('categories',)
    ordering = ['categories', 'name']


@admin.register(WordCategory)
class WordCategoryAdmin(admin.ModelAdmin):
    list_filter = ('category',)
    ordering = ['category', 'word']
