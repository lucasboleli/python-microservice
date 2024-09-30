from django.test import TestCase
from django.urls import reverse

# from rest_framework.test import APIClient
import pytest
import requests

from admin.products.models import Product

# response = requests.get(endpoint)

@pytest.fixture
def create_product():
    return Product.objects.create()


def test_can_call_endpoint():
    response = requests.get("http://localhost:8000/api/products")

    assert response.status_code == 200
    assert isinstance(xx,Product)
    assert Products.objects.all().count() == 1
