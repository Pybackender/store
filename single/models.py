from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
# Create your models here.


class Single(models.Model):
    name = models.CharField(max_length=125)
    slug = models.SlugField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(null=True,blank=True)
    sold = models.IntegerField(null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    stars = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    content = models.CharField(max_length=225)
    piece_available = models.IntegerField()

    class Meta:
        verbose_name = "single"
        verbose_name_plural = "singles"

    indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
        ]    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.id, self.slug])

class Description(models.Model):
    name = models.CharField(max_length=125)
    content = models.CharField(max_length=500)

    class Meta:
        verbose_name = "Description"
        verbose_name_plural = "Descriptions"

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    title = models.CharField(max_length=125)
    content = models.CharField(max_length=500)

    class Meta:
        verbose_name = "Manufacturer"
        verbose_name_plural = "Manufacturers"

    def __str__(self):
        return self.title

class Review(models.Model):
    name = models.CharField(max_length=125)
    date = models.DateField()
    content = models.CharField(max_length=500)
    image = models.ImageField(null=True,blank=True)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self):
        return self.name
