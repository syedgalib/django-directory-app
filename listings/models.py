from django.db import models
from django.utils import timezone


# Listings Model
class Listing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default='', null=True)
    slug = models.SlugField(unique=True)
    term_id = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
