from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from rest_framework import status
from .models import Employee, Customer, User
from .serializer import EmployeeSerializer, CustomerSerializer
import json


# =========================== Register Section ============================
@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parse JSON data
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data.'}, status=400)
        
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        print(name, email, password)

        # Check if email already exists
        if User.email_exists(email):
            return JsonResponse({'error': 'Email already exists.'}, status=400)

        # Hash the password and create the user
        hashed_password = make_password(password)
        user = User.objects.create(name=name, email=email, password=hashed_password)
        user.save()
        return JsonResponse({'message': 'User registered successfully.'}, status=201)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)


# =========================== Login Section ============================
@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')

            print(data)

            if not email or not password:
                print("email and password are required.")
                return JsonResponse({'error': 'email and password are required.'}, status=400)

            try:
                user = User.objects.get(email=email)
                if check_password(password, user.password):
                    print("Login successful")
                    response = JsonResponse({'message': 'Login successful'}, status=200)
                    return response
                else:
                    print("Invalid password")
                    return JsonResponse({'error': 'Invalid password'}, status=400)

            except User.DoesNotExist:
                print("Invalid username")
                return JsonResponse({'error': 'Invalid username'}, status=400)

        except json.JSONDecodeError:
            print("Invalid JSON data")
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

    print("Invalid request method")
    return JsonResponse({'error': 'Invalid request method'}, status=405)


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
def view_all_employee(request, pk):
    if pk > 0:
        query = Employee.objects.all()
        limit = 10
        offset = (pk - 1) * limit        # offset (from) to (offset + 10)
        number_of_pages = len(query) / limit

        if offset + limit > len(query):
            to_value = offset + (len(query) - offset)
        else:
            to_value = offset + limit
        
        filter_records = query[offset:to_value]

        if isinstance(number_of_pages, float):
            number_of_pages = int(number_of_pages) + 1

        serializer = EmployeeSerializer(filter_records, many=True)
        return JsonResponse([{"total_page": number_of_pages}] + serializer.data, safe=False)
    
    return JsonResponse({'message': 'invalid page number. it hastobe > 0'})


# Update Employee data
@api_view(['PUT'])
def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    serializer = EmployeeSerializer(employee, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Delete Employee
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return JsonResponse({'message': 'Removed employee from database.'}, status=201)


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
def view_all_customer(request, pk):
    if pk > 0:
        query = Customer.objects.all()
        limit = 10
        offset = (pk - 1) * limit        # offset (from) to (offset + 10)
        number_of_pages = len(query) / limit

        if offset + limit > len(query):
            to_value = offset + (len(query) - offset)
        else:
            to_value = offset + limit
        
        filter_records = query[offset:to_value]

        if isinstance(number_of_pages, float):
            number_of_pages = int(number_of_pages) + 1

        serializer = CustomerSerializer(filter_records, many=True)
        return JsonResponse([{"total_page": number_of_pages}] + serializer.data, safe=False)
    
    return JsonResponse({'message': 'invalid page number. it hastobe > 0'})


# Update Customer data
@api_view(['PUT'])
def update_customer(request, pk):
    customer = get_object_or_404(Employee, pk=pk)
    serializer = CustomerSerializer(customer, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete_customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    return JsonResponse({'message': 'Removed customer from database.'}, status=201)
