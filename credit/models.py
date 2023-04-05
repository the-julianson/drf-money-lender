from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.


class LoanRequest(models.Model):
    personal_id = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    requested_amount = models.PositiveIntegerField(
        validators=[MinValueValidator(1000), MaxValueValidator(310000)]
    )
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Loan request for personal ID: {self.personal_id}"
