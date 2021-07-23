from django.db import models
from django.utils import timezone


# Create your models here.
class Listing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
