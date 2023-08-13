from django.urls import path
from employees import views

urlpatterns = [
    path('', views.EmployeeList.as_view(), name="employee-list"),
    path('<int:pk>/', views.EmployeeDetail.as_view(), name="employee-detail")
]
