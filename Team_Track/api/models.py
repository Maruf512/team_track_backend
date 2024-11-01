from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=300)
    roll = models.CharField(max_length=50)

    def __str__(self):
        return self.name    

class Employee(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    mobile = models.CharField(max_length=50)
    nid_no = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    mobile = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    image = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Invoice_Challan(models.Model):
    customer_uid = models.CharField(max_length=100)
    produced_goods = models.TextField()
    grand_total = models.CharField(max_length=100)
    created_at = models.DateTimeField()

class Cash_Memo(models.Model):
    invoice_id = models.CharField(max_length=100)
    total_quantity_yds = models.CharField(max_length=200)
    rate = models.CharField(max_length=100)
    total_tk = models.CharField(max_length=100)
    created_at = models.DateTimeField()

class Pay_Employee(models.Model):
    invoice_id = models.CharField(max_length=200)
    employee_id = models.CharField(max_length=200)
    total_yds = models.CharField(max_length=100)
    rate = models.CharField(max_length=100)
    total_tk = models.CharField(max_length=100)
    due = models.CharField(max_length=100)


class Sell_Invoice(models.Model):
    products_details = models.TextField()
    total_price = models.CharField(max_length=100)
    customer_id = models.CharField(max_length=50)


