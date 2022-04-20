from django.db import models

# Create your models here.
class URL(models.Model):
    link = models.CharField(max_length=100000)
    short_link_id = models.CharField(max_length=10)