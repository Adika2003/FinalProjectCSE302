from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=200)
    reg_no = models.CharField(max_length=50, blank=True)
    role = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='members/', blank=True, null=True)
    club = models.ForeignKey(
        'clubs.Club',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='members'
    )

    def __str__(self):
        return self.name
