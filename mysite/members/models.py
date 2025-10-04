from django.db import models

class Member(models.Model):
    ROLE_TYPE = [
        ('convener', 'Convener'),
        ('executive', 'Executive Member'),
        ('general', 'General Member'),
    ]

    name = models.CharField(max_length=200)
    role_type = models.CharField(max_length=20, choices=ROLE_TYPE, default='general')
    role = models.CharField(max_length=100, blank=True)
    batch = models.CharField(max_length=50, blank=True)
    reg_no = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    photo = models.ImageField(upload_to='members/', blank=True, null=True)

    club = models.ForeignKey(
        'clubs.Club',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='members'
    )

    def __str__(self):
        return f"{self.name} ({self.role})"
