import pytest

from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_lettings_index_view(letting):
    client = Client()
    path = reverse("lettings:index")
    response = client.get(path)
    content = response.content.decode()

    assert letting.title in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/lettings_index.html")


@pytest.mark.django_db
def test_lettings_detail_view(letting):
    client = Client()
    path = reverse("lettings:letting", kwargs={"letting_id": 1})
    response = client.get(path)
    content = response.content.decode()

    assert letting.address.country_iso_code in content
    assert response.status_code == 200
    assertTemplateUsed(response, "lettings/letting.html")
