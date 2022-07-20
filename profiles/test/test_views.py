import pytest
from django.test import TestCase, Client
from django.urls import reverse
from profiles.models import Profile, User
from pytest_django.asserts import assertTemplateUsed

# Create your tests here.

@pytest.mark.django_db
def test_index():
    client = Client()
    path = reverse('profiles_index')
    response = client.get(path)
    content = response.content.decode()

    assert "Profiles" in content
    assert response.status_code == 200
    assertTemplateUsed(response, 'profiles/index.html')

@pytest.mark.django_db
def test_profile():
    client = Client()
    User.objects.create(username = "JeanTest")
    Profile.objects.create(user = User.objects.get(username = "JeanTest"))
    path = reverse('profile', kwargs={'username': "JeanTest"})
    response = client.get(path)
    content = response.content.decode()
    
    assert "JeanTest" in content
    assert response.status_code == 200
    assertTemplateUsed(response, 'profiles/profile.html') 