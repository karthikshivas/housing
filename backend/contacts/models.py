from django.db import models
from datetime import datetime

class Contact(models.Model):
    email = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    subject = models.CharField(max_length=150)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.email