from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class LoanRequest(models.Model):
    personal_id = models.CharField(max_length=20)
    dni = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    requested_amount = models.DecimalField(max_digits=10, decimal_places=2)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Loan request for personal ID: {self.personal_id}"
