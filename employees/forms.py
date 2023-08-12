from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Employee


class EmployeeCreationForm(UserCreationForm):
    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeChangeForm(UserChangeForm):
    class Meta:
        model = Employee
        fields = '__all__'
