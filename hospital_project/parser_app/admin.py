from django.contrib import admin

from .models import Category, Links, Info


@admin.register(Category)
class KeywordsAdmin(admin.ModelAdmin):
    list_display = ('name_category', 'cities', 'links_on_cities')


@admin.register(Links)
class LinksAdmin(admin.ModelAdmin):
    list_display = ('links_on_hospital',)


@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    list_display = ('name_hospital', 'number_phone', 'overview', 'ratings', 'col_vo_reviews')