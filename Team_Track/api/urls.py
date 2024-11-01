from django.urls import path
from .views import add_employee, view_all_employee, add_customer, view_all_customer


urlpatterns = [
    # Employee Routing
    path('employee/create/', add_employee.as_view(), name="add_employee"),
    path('employee/view/', view_all_employee, name="view_all_employee"),

    # Customer Routing
    path('customer/create/', add_customer.as_view(), name="add_customer"),
    path('customer/view/', view_all_customer, name="view_all_customer"),
]


