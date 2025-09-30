from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=255, blank=True)
    club = models.ForeignKey(
        'clubs.Club',
        on_delete=models.CASCADE,
        related_name='events'
    )

    def __str__(self):
        return self.title
