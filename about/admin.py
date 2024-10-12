from django.contrib import admin

from about.models import About, Liquid


@admin.register(About)
class Aboutadmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'since','experience']


@admin.register(Liquid)
class Liquidadmin(admin.ModelAdmin):
    list_display = ['name','image']
