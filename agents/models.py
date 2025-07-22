from django.db import models
from django.contrib.auth.models import User
import uuid

class AgentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    identity_card = models.FileField(upload_to='identity_cards/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Agent {self.user.username} - ID: {self.unique_id}"