from django.contrib import admin

from info.models import Info

# Register your models here.
@admin.register(Info)
class Infoadmin(admin.ModelAdmin):
    list_display = ['name', 'content', 'address','phone']