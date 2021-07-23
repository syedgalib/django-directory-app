from django.db import models
from django.utils import timezone


# Taxonomy Model
class Taxonomy(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default='', null=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


# Term Model
class Term(models.Model):
    title = models.CharField(max_length=255)
    taxonomy_id = models.ForeignKey(Taxonomy, on_delete=models.CASCADE)
    description = models.TextField(default='', null=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
