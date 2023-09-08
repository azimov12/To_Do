from django.db import models
# Create your models here.

class ToDo(models.Model):
    task_name = models.CharField(max_length=32, default= "")
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    status = models.CharField(max_length=25, default = "Not Done")
    desc = models.CharField(default='')
    