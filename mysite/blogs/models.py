from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    author = models.CharField(max_length=200)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    club = models.ForeignKey(
        'clubs.Club',
        on_delete=models.CASCADE,
        related_name='posts'
    )

    def __str__(self):
        return self.title
