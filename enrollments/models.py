from django.db import models
from django.contrib.auth.models import User
from training.models import trainings
# Create your models here.
class enrolls(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    training = models.ForeignKey(trainings, on_delete=models.CASCADE)
    enroll_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now=False)
