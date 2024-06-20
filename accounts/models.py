from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from crm_system import settings

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)  # Make sure this matches the recent migration change
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class Lead(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.customer.name} - {self.status}"

class Opportunity(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    close_date = models.DateField()

    def __str__(self):
        return f"{self.lead.customer.name} - {self.value}"

class Interaction(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    note = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.lead.customer.name} - {self.date}"
    

class CustomUser(AbstractUser):
    # Add any additional fields you want here
    pass

    def __str__(self):
        return self.username
