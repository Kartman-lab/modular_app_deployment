import pytest


@pytest.mark.django_db
def test_profile_str(profile):
    assert str(profile.user.username) == "arnaud"
    assert str(profile.favorite_city) == "Lyon"
