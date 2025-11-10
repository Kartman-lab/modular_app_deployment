from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """Représente l'adresse d'un bien immobilier."""

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        """Retourne une représentation lisible de l'adresse (numéro + rue)."""
        return f"{self.number} {self.street}"


class Letting(models.Model):
    """Représente un bien immobilier avec un titre et son adresse associée."""

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Lettings"

    def __str__(self):
        """Retourne le titre du bien immobilier."""
        return self.title
