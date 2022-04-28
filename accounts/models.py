from random import choices
from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    CATEGORY = (
        ('Lawyer', 'Lawyer'),
        ('Doctor', 'Doctor')
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    PAYMENT_STATUS = (
        ('Pending', 'Pending'),
        ('Done', 'Done'),
    )
    customer_id = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True)
    service_id = models.ForeignKey(
        Service, on_delete=models.SET_NULL, null=True)
    payment_status = models.CharField(
        max_length=200, null=True, choices=PAYMENT_STATUS)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
