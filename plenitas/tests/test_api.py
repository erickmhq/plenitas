import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from django.urls import reverse
from devices.models import Device

User = get_user_model()

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user(db):
    def make_user(**kwargs):
        kwargs.setdefault("email", "test@example.com")
        kwargs.setdefault("password", "password123")
        user = User.objects.create_user(**kwargs)
        return user
    return make_user

@pytest.fixture
def auth_user_client(api_client, create_user):
    user = create_user()
    url = reverse("token-obtain")
    response = api_client.post(url, {
        "email": user.email,
        "password": "password123"
    })
    token = response.data["access"]
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    return user, api_client

@pytest.mark.django_db
def test_user_registration(api_client):
    url = reverse("user-register")
    response = api_client.post(url, {
        "email": "newuser@example.com",
        "password": "newpassword123"
    })
    assert response.status_code == 201
    assert User.objects.filter(email="newuser@example.com").exists()

def test_login_returns_token(api_client, create_user):
    user = create_user(email="tokenuser@example.com", password="secretpass")
    url = reverse("token-obtain")
    response = api_client.post(url, {
        "email": "tokenuser@example.com",
        "password": "secretpass"
    })
    assert response.status_code == 200
    assert "access" in response.data
    assert "refresh" in response.data

@pytest.mark.django_db
def test_get_devices_authenticated(auth_user_client):
    user, client = auth_user_client
    Device.objects.create(user=user, name="Switch", ip="192.168.1.1", is_active=True)
    url = reverse("device-list-create")
    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.data, list)
    assert any(device["name"] == "Switch" for device in response.data)

@pytest.mark.django_db
def test_create_device(auth_user_client):
    user, client = auth_user_client
    payload = {
        "name": "Router",
        "ip": "192.168.0.1",
        "is_active": True
    }
    url = reverse("device-list-create")
    response = client.post(url, payload)
    assert response.status_code == 201
    assert Device.objects.filter(user=user, name="Router").exists()
