from django.contrib import admin

from .models import Women, Category, Genre

from mptt.admin import MPTTModelAdmin


class GenreInline(admin.TabularInline):
    model = Genre



admin.site.register(Women)
admin.site.register(Genre, MPTTModelAdmin)
admin.site.register(Category)