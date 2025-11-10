import pytest
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.fixture
def user(db):
    """Crée un utilisateur Django basique."""
    return User.objects.create_user(username="arnaud", password="test123")


@pytest.fixture
def profile(user):
    """Crée un profil associé à l'utilisateur précédent."""
    return Profile.objects.create(user=user, favorite_city="Lyon")
