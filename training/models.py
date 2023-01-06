from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class trainings(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=500,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
