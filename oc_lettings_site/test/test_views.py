from django.test import TestCase, Client
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

# Create your tests here.

def test_index():
    client = Client()
    path = reverse('index')
    response = client.get(path)
    content = response.content.decode()

    assert "Holiday Homes" in content
    assert response.status_code == 200
    assertTemplateUsed(response, 'index.html')