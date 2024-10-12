from django.db import models
from django.core.validators import validate_email

class Contactus(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(
                              validators=[validate_email])
    subject = models.CharField(max_length=15,blank=True,null=True)
    message = models.TextField()

    class Meta:
        verbose_name = "contactus"
        verbose_name_plural = "contactsus"

    def __str__(self):
        return self.name
    
class Company(models.Model):
    address = models.CharField(max_length=225)    
    phone = models.IntegerField()    
    email = models.EmailField(max_length=225)    
    website = models.CharField(max_length=225)   

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Company"

    def __str__(self):
        return self.email 