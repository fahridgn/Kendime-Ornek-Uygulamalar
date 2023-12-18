from django.db import models

# Create your models here.


class Theme(models.Model):
    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    attrs = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
