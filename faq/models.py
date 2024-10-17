from django.db import models
from django.utils import timezone


class Faq(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
        
    title = models.CharField(max_length=125)
    slug = models.SlugField(max_length=125)
    content = models.TextField(null=True, blank=True) 
    link = models.CharField(max_length=125, null=True, blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "faq"
        verbose_name_plural = "FAQs"  # Updated plural form
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title if self.title else "Untitled FAQ"  # Handling None case

