from django.db import models
from django.contrib.auth.models import User

class Wish(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    wish_text = models.TextField()
    image = models.ImageField(upload_to='wish_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}'s Wish"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    has_lit_diyas = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class GlobalStats(models.Model):
    total_diyas = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Global Stats - {self.total_diyas} Diyas Lit"
