from typing import Any
from django.db import models
from django.urls import reverse


class Club(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='club_logos/', blank=True, null=True)

    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.events = None
        self.members = None

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('clubs:detail', args=[self.slug])
