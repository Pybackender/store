from django.contrib import admin

from offering.models import Offering

# Register your models here.
@admin.register(Offering)
class Offeringadmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'price','last_price']