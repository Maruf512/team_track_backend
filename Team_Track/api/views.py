from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Employee, Customer
from .serializer import EmployeeSerializer, CustomerSerializer


# =========================== Employee Section ============================
# Add New Employee
class add_employee(APIView):
    def post(self, requset):
        serializer = EmployeeSerializer(data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# View All Employee
def view_all_employee(request):
    query = Employee.objects.all()
    serializer = EmployeeSerializer(query, many=True)
    return JsonResponse(serializer.data, safe=False)


# =========================== Customer Section ============================
# Add New Customer
class add_customer(APIView):
    def post(self, requset):
        serializer = CustomerSerializer(data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# View all Customer
def view_all_customer(request):
    query = Customer.objects.all()
    serializer = CustomerSerializer(query, many=True)
    return JsonResponse(serializer.data, safe=False)

