from django.db import models
from django.contrib.auth.models import User
import uuid

LOAN_TYPES = [
    ('HOME', 'Home Loan'),
    ('CAR', 'Car Loan'),
    ('PERSONAL', 'Personal Loan'),
    ('BUSINESS', 'Business Loan'),
    ('OTHER', 'Other'),
]

class Lead(models.Model):
    # unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    customer_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    loan_type = models.CharField(max_length=20, choices=LOAN_TYPES)
    agent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leads')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Lead for {self.customer_name} by {self.agent.username}"