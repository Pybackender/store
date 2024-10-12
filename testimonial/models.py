from django.db import models

# Create your models here.


class Comment(models.Model):
    name = models.CharField(max_length=125)
    content = models.CharField(max_length=125)
    image = models.ImageField(null=True, blank=True)
    position = models.CharField(max_length=125)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.name


class Experiense(models.Model):
    title = models.CharField(max_length=125)
    number = models.IntegerField()

    class Meta:
        verbose_name = "Experiense"
        verbose_name_plural = "Experienses"

    def __str__(self):
        return self.title