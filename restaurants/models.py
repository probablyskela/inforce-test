# Create your models here.
from datetime import date

from django.db import models

from employees.models import Employee


class Restaurant(models.Model):
    owner = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="restaurant name", max_length=200)
    address = models.TextField()

    def __str__(self) -> str:
        return self.name


class Dish(models.Model):
    name = models.CharField(verbose_name="dish name", max_length=200)

    def __str__(self) -> str:
        return self.name


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="menu name", max_length=200)
    publication_date = models.DateField(default=date.today)

    dishes = models.ManyToManyField(Dish)

    def __str__(self) -> str:
        return self.name


class Vote(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    publication_date = models.DateField(default=date.today)

    def __str__(self) -> str:
        return f"{self.employee.first_name} > {self.menu.name}"
