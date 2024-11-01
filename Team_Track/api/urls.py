from django.urls import path
from .views import register_user, add_employee, view_all_employee, add_customer, view_all_customer, update_customer, update_employee


urlpatterns = [
    # Employee Routing
    path('employee/create/', add_employee.as_view(), name="add_employee"),
    path('employee/view/', view_all_employee, name="view_all_employee"),
    path('employee/update/<int:pk>/', update_employee, name="update_employee"),

    # Customer Routing
    path('customer/create/', add_customer.as_view(), name="add_customer"),
    path('customer/view/', view_all_customer, name="view_all_customer"),
    path('customer/update/<int:pk>/', update_customer, name="update_customer"),

    path('register/', register_user, name="register_user"),


]


