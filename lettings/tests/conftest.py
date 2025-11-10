import pytest
from lettings.models import Address, Letting


@pytest.fixture
def address(db):
    return Address.objects.create(
        number=10,
        street="Main Street",
        city="LA",
        state="CA",
        zip_code=90001,
        country_iso_code="USA",
    )


@pytest.fixture
def letting(db, address):
    return Letting.objects.create(title="Beautiful house", address=address)
