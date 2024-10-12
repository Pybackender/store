from django.db import models

# Create your models here.
class Offering(models.Model):
    name = models.CharField(max_length=125)
    type = models.CharField(max_length=125)
    image = models.ImageField(null=True,blank=True)
    price = models.IntegerField()
    last_price = models.IntegerField(null=True,blank=True)
    link =models.CharField(max_length=125,null=True,blank=True)
    best_seller = models.BooleanField(default=False)
    new_arrival = models.BooleanField(default=False)
    on_sale = models.BooleanField(default=False)
    class Meta:
        verbose_name = "offering"
        verbose_name_plural = "offerings"

    def __str__(self):
        return self.name