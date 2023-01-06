from django.db import models
from section.models import sections


# Create your models here.
class sub_sections(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,blank=False)
    order_id = models.IntegerField(blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=2000,blank=True)
    section = models.ForeignKey(sections, on_delete=models.CASCADE)


class references(models.Model):
    id = models.AutoField(primary_key=True)
    files = models.FileField(upload_to='uploads/')
    urls = models.URLField(max_length=200, blank=True)
    section = models.ForeignKey(sections, on_delete=models.CASCADE)
    sub_section = models.ForeignKey(sub_sections, on_delete=models.CASCADE)
