

from django.db import models
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import random
import uuid

# Create your models here.
# class Contact(models.Model):
#     fname = models.CharField(max_length=25)
#     lname = models.CharField(max_length=25)
#     phone = models.CharField(max_length=10)
#     email = models.CharField(max_length=50)
#     comment = models.TextField()
#     date = models.DateField()
        
#     def __str__(self):
#         return self.fname

class BaseModel(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    class Meta:
        abstract=True