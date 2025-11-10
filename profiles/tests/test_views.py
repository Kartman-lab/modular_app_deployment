import pytest

from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_profile_index_view(profile):
    client = Client()
    path = reverse("profiles:index")
    response = client.get(path)
    content = response.content.decode()

    assert profile.user.username in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/profiles_index.html")


@pytest.mark.django_db
def test_profile_details_view(profile):
    client = Client()
    path = reverse("profiles:profile", kwargs={"username": "arnaud"})
    response = client.get(path)
    content = response.content.decode()

    assert profile.favorite_city in content
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/profile.html")
