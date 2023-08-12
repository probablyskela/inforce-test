from rest_framework import generics

from employees.models import Employee
from employees.serializers import EmployeeSerializer


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetail(
    generics.RetrieveUpdateDestroyAPIView,
):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
