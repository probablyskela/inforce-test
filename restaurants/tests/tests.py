from datetime import date

import pytest
from django.shortcuts import get_object_or_404
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from employees.models import Employee
from restaurants.models import Dish, Menu, Restaurant
from restaurants.tests.fixtures import authenticated_client, test_user


@pytest.mark.django_db
class TestRestaurantViews:
    def test_create_restaurant(self):
        employee = Employee.objects.create_superuser(
            email="op@gmail.com", password="password"
        )
        client = APIClient()
        client.force_authenticate(user=employee)

        response = client.post(
            reverse("restaurant-list"),
            {"name": "Test Restaurant", "address": "Test Address"},
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert Restaurant.objects.count() == 1
        assert Restaurant.objects.get().name == "Test Restaurant"
        assert Restaurant.objects.get().address == "Test Address"
        assert Restaurant.objects.get().owner == employee

    def test_get_all_restaurants(self, authenticated_client: APIClient):
        authenticated_client.post(
            reverse("restaurant-list"),
            {"name": "Test 1", "address": "Test 1"},
        )
        authenticated_client.post(
            reverse("restaurant-list"),
            {"name": "Test 2", "address": "Test 2"},
        )

        response = authenticated_client.get(reverse("restaurant-list"))

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2

    def test_vote_for_irrelevant_offer(self, authenticated_client: APIClient):
        restaurant = authenticated_client.post(
            reverse("restaurant-list"),
            {"name": "Test 1", "address": "Test 1"},
        )
        dish = authenticated_client.post(reverse("dishes-list"), {"name": "test"})
        restaurant = get_object_or_404(Restaurant, pk=restaurant.data["id"])
        dish_obj = get_object_or_404(Dish, pk=dish.data["id"])
        menu = Menu.objects.create(
            name="Test",
            restaurant=restaurant,
            publication_date=date(year=2000, month=1, day=1),
        )
        menu.dishes.add(dish_obj)
        menu.save()

        response = authenticated_client.post(
            reverse("offers-vote", kwargs={"pk": menu.id})
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
