from django.db import models
from training.models import trainings
# Create your models here.
class sections(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,blank=False)
    order_id = models.IntegerField(blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=2000,blank=True)
    training = models.ForeignKey(trainings, on_delete=models.CASCADE)