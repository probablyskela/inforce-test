import pytest
from rest_framework.test import APIClient

from employees.models import Employee


@pytest.fixture
def test_user() -> Employee:
    employee = Employee.objects.create_superuser(
        email="test@gmail.com", password="test"
    )
    return employee


@pytest.fixture
def authenticated_client(test_user) -> APIClient:
    client = APIClient()
    client.force_authenticate(user=test_user)
    return client
