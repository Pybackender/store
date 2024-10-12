from django.contrib import admin

from contact.models import Company, Contactus

# Register your models here.
@admin.register(Contactus)
class ContactusAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject']
    search_fields = ['name']

    actions = ['make_published', 'make_draft',
               'export_as_json', 'export_as_csv']
    
@admin.register(Company)
class ContactusAdmin(admin.ModelAdmin):
    list_display = ['address', 'email', 'phone']