from django.db import models
from datetime import datetime

# Create your models here.

class Realtor(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    photos = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    top_seller = models.BooleanField(default=False)
    date_hired = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
