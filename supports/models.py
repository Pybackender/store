from django.db import models

# Create your models here.
class Support(models.Model):
    title = models.CharField(max_length=125)
    content = models.CharField(max_length=225)
    icons = models.CharField(max_length=125,null=True,blank=True)

    class Meta:
        verbose_name = "support"
        verbose_name_plural = "supports"

    def __str__(self):
        return self.title