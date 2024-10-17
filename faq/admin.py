from django.contrib import admin

from faq.models import Faq

@admin.register(Faq)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug',  'publish']
    list_filter = ['created', 'publish']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}