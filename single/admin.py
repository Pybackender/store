from django.contrib import admin

from single.models import Description, Manufacturer, Review, Single

# Register your models here.


@admin.register(Single)
class Singleadmin(admin.ModelAdmin):
    list_display = ['name', 'content','price','piece_available']


@admin.register(Description)
class Descriptionadmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Manufacturer)
class Manufactureradmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Review)
class Reviewadmin(admin.ModelAdmin):
    list_display = ['name','date']
