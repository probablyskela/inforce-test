from datetime import date

from django.http import Http404
from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from employees.models import Employee
from restaurants.models import Dish, Menu, Restaurant, Vote
from restaurants.permissions import IsAdminOrReadOnly
from restaurants.serializers.dish_serializer import DishSerializer
from restaurants.serializers.menu_serializer import MenuSerializer
from restaurants.serializers.restaurant_serializer import RestaurantSerializer
from restaurants.serializers.vote_serializer import VoteSerializer


class RestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer: RestaurantSerializer):
        owner_id = self.request.user.id
        owner = get_object_or_404(Employee, pk=owner_id)
        serializer.save(owner=owner)


class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAdminOrReadOnly]


class MenusList(generics.ListCreateAPIView):
    serializer_class = MenuSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        restaurant_pk = self.kwargs["pk"]
        return Menu.objects.filter(restaurant_id=restaurant_pk)

    def perform_create(self, serializer: MenuSerializer):
        restaurant_pk = self.kwargs["pk"]
        restaurant = get_object_or_404(Restaurant, pk=restaurant_pk)
        serializer.save(restaurant=restaurant)


class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAdminOrReadOnly]


class CurrentMenusList(generics.ListAPIView):
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Menu.objects.filter(publication_date=date.today())


class CurrentMenusDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        menu = (
            Menu.objects.annotate(num_votes=Count("vote"))
            .order_by("-num_votes")
            .first()
        )

        if not menu:
            raise Http404("No available menus")
        serializer = MenuSerializer(menu)
        return Response(serializer.data)


class VoteDetail(generics.CreateAPIView):
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer: VoteSerializer):
        employee_id = self.request.user.id
        employee = get_object_or_404(Employee, pk=employee_id)
        menu_id = self.kwargs["pk"]
        menu = get_object_or_404(Menu, pk=menu_id)

        # Verify that menu is relevant
        if menu.publication_date != date.today():
            raise ValidationError(
                code=status.HTTP_400_BAD_REQUEST,
                detail="Menu's publication date is not today",
            )

        # Delete all employee's votes to current menus
        today = date.today()
        Vote.objects.filter(employee=employee, menu__publication_date=today).delete()

        serializer.save(employee=employee, menu=menu)


class DishList(generics.ListCreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAdminOrReadOnly]


class DishDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAdminOrReadOnly]
