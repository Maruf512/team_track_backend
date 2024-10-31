# Generated by Django 5.1.2 on 2024-10-31 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Add_Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=50)),
                ('nid_no', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cash_Memo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_id', models.CharField(max_length=100)),
                ('total_quantity_yds', models.CharField(max_length=200)),
                ('rate', models.CharField(max_length=100)),
                ('total_tk', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Invoice_Challan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_uid', models.CharField(max_length=100)),
                ('produced_goods', models.TextField()),
                ('grand_total', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Pay_Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_id', models.CharField(max_length=200)),
                ('employee_id', models.CharField(max_length=200)),
                ('total_yds', models.CharField(max_length=100)),
                ('rate', models.CharField(max_length=100)),
                ('total_tk', models.CharField(max_length=100)),
                ('due', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Sell_Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products_details', models.TextField()),
                ('total_price', models.CharField(max_length=100)),
                ('customer_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=300)),
                ('roll', models.CharField(max_length=50)),
            ],
        ),
    ]
