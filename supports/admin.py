from django.contrib import admin

from supports.models import Support

# Register your models here.
@admin.register(Support)
class Supportadmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'icons']