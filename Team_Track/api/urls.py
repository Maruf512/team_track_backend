from django.urls import path
from .views import add_employee


urlpatterns = [
    path('employee/', add_employee.as_view(), name="add_employee")
]


