import pytest
from django.urls import reverse
from django.test import Client
from lettings.models import Address, Letting
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_index():
    client = Client()
    path = reverse('lettings_index')
    response = client.get(path)
    content = response.content.decode()
    assert "Lettings" in content
    assert response.status_code == 200
    assertTemplateUsed(response, 'lettings/index.html')


@pytest.mark.django_db
def test_letting():
    client = Client()
    Address.objects.create(
        number=223,
        street="Baker",
        city="London",
        zip_code=5208,
        country_iso_code='WR6'
    )
    Letting.objects.create(
        title="Testare",
        address=Address.objects.get(street="Baker"),
    )
    path = reverse(
        'letting', kwargs={'letting_id': 1}
    )
    response = client.get(path)
    content = response.content.decode()
    assert "Testare" in content
    assert response.status_code == 200
    assertTemplateUsed(response, 'lettings/letting.html')
