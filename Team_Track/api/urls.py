from django.urls import path
from .views import register_user, login_user, delete_customer, delete_employee, add_employee, view_all_employee, add_customer, view_all_customer, update_customer, update_employee


urlpatterns = [
    # User Routing
    path('register/', register_user, name="register_user"),
    path('login/', login_user, name="login_user"),

    # Employee Routing
    path('employee/create/', add_employee.as_view(), name="add_employee"),
    path('employee/view/<int:pk>/', view_all_employee, name="view_all_employee"),
    path('employee/update/<int:pk>/', update_employee, name="update_employee"),
    path('employee/delete/<int:pk>/', delete_employee, name="delete_employee"),

    # Customer Routing
    path('customer/create/', add_customer.as_view(), name="add_customer"),
    path('customer/view/', view_all_customer, name="view_all_customer"),
    path('customer/update/<int:pk>/', update_customer, name="update_customer"),
    path('customer/delete/<int:pk>/', delete_customer, name="delete_customer"),



]


