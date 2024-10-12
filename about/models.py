from django.db import models


class About(models.Model):
    title = models.CharField(max_length=125)
    content = models.CharField(max_length=225)
    image = models.ImageField(null=True, blank=True)
    since = models.IntegerField()
    experience = models.IntegerField()

    class Meta:
        verbose_name = "about"
        verbose_name_plural = "abouts"

    def __str__(self):
        return self.title


class Liquid(models.Model):
    name = models.CharField(max_length=125)
    image = models.ImageField(null=True, blank=True)
