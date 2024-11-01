from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from rest_framework import status
from .models import Employee, Customer, User
from .serializer import EmployeeSerializer, CustomerSerializer, UserSerializer
import json


# =========================== Register Section ============================
@csrf_exempt
def register_user(request):
    if request.method == "POST":
        print("++++++++++++++++++++++++++++++++++++++++++++++++++")
        try:
            data = json.loads(request.body)  # Parse JSON data
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data."}, status=400)

        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        print(name)

        # Check if email already exists
        if User.email_exists(email):
            return JsonResponse({"error": "Email already exists."}, status=400)

        # Hash the password and create the user
        hashed_password = make_password(password)
        user = User.objects.create(name=name, email=email, password=hashed_password)
        return JsonResponse({"message": "User registered successfully."}, status=201)

    return JsonResponse({"error": "Invalid request method."}, status=405)


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


# Update Employee data
@api_view(["PUT"])
def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    serializer = EmployeeSerializer(employee, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


@api_view(["PUT"])
def update_customer(request, pk):
    customer = get_object_or_404(Employee, pk=pk)
    serializer = CustomerSerializer(customer, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
