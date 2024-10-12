from django.contrib import admin

from store.models import Category, Product

# Register your models here.
@admin.register(Product)
class Portadmin(admin.ModelAdmin):
    list_display = [ 'name','category','image',]
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title" , "slug"]
    prepopulated_fields = {'slug': ('title',)}