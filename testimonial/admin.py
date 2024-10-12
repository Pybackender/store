from django.contrib import admin

from testimonial.models import Comment, Experiense

# Register your models here.
@admin.register(Comment)
class Commentadmin(admin.ModelAdmin):
    list_display = ['name', 'content', 'position']

@admin.register(Experiense)
class Experienseadmin(admin.ModelAdmin):
    list_display = ['title', 'number']