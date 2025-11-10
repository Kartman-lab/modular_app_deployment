import pytest
from django.urls import reverse, resolve


@pytest.mark.django_db
def test_profile_index_url():
    path = reverse("profiles:index")
    assert resolve(path).view_name == "profiles:index"


@pytest.mark.django_db
def test_profile_detail_url():
    path = reverse("profiles:profile", kwargs={"username": "arnaud"})
    assert resolve(path).view_name == "profiles:profile"
