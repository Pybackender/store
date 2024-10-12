from django.db import models


class Info(models.Model):
    name = models.CharField(max_length=125)
    content = models.CharField(max_length=125)
    address = models.URLField(max_length=200,null=True, blank=True)
    phone = models.IntegerField(null=True)
    telegram = models.CharField(max_length=125, null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    facebook = models.URLField(max_length=125, null=True, blank=True)
    discord = models.URLField(max_length=125, null=True, blank=True)

    class Meta:
        verbose_name = "Info"
        verbose_name_plural = "Infos"

    def __str__(self):
        return self.name
