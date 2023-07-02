from django.contrib import admin

from .models import Category, City, ClinicLink, ClinicInfo


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name_category', 'link', 'status')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'link', 'status')


@admin.register(ClinicLink)
class ClinicLinkAdmin(admin.ModelAdmin):
    list_display = ('category', 'city', 'link', 'status')


@admin.register(ClinicInfo)
class ClinicInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'practicing_physicians_count', 'address', 'number_phone', 'overview')
