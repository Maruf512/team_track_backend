from rest_framework import serializers
from .models import User, Employee, Customer, Products, Sell_Invoice, Invoice_Challan, Pay_Employee, Cash_Memo


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class Sell_InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sell_Invoice
        fields = '__all__'


class Invoice_ChallanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice_Challan
        fields = '__all__'


class Pay_EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pay_Employee
        fields = '__all__'


class Cash_MemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cash_Memo
        fields = '__all__'

