from django.contrib import admin
from .models import NewCategory, News


@admin.register(NewCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'date_added')
    list_filter = ('category_name', 'date_added')
    search_fields = ('category_name', 'date_added')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_added')
    list_filter = ('category', 'date_added')
    search_fields = ('title', 'text')


