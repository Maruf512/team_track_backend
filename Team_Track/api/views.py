from rest_framework import generics
from .models import Add_Employee
from .serializer import Add_EmployeeSerializer

# Create your views here.
class add_employee(generics.ListCreateAPIView):
    queryset = Add_Employee.objects.all()
    serializer_class = Add_EmployeeSerializer
