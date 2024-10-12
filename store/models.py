from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    class Meta:
        ordering = ['title']
    indexes = [
        models.Index(fields=['title']),
    ]
    verbose_name = 'category'
    verbose_name_plural = 'categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('store:product_list_by_category', args=[self.slug])


class Product(models.Model):
    name = models.CharField(max_length=125)
    slug = models.SlugField(max_length=200)
    type = models.CharField(max_length=125)
    image = models.ImageField(null=True, blank=True,
                              upload_to='product/%Y/%m/%d')
    price = models.IntegerField()
    last_price = models.IntegerField(null=True, blank=True)
    link = models.CharField(max_length=125, null=True, blank=True)
    best_seller = models.BooleanField(default=False)
    new_arrival = models.BooleanField(default=False)
    on_sale = models.BooleanField(default=False)
    category = models.ForeignKey(Category,
                                 related_name='Product',
                                 on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.id, self.slug])
