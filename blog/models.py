from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=125)
    content = models.CharField(max_length=125)
    image = models.ImageField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    link = models.CharField(max_length=125, null=True, blank=True)

    class Meta:
        verbose_name = "blog"
        verbose_name_plural = "blogs"

    def __str__(self):
        return self.title
