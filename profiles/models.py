from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Représente le profil d'un utilisateur."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    class Meta:
        verbose_name_plural = "Profiles"

    def __str__(self):
        """Retourne le nom d'utilisateur associé au profil."""
        return self.user.username
