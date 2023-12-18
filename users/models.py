from django.db import models


# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=120)
    salary = models.CharField(max_length=120)
    department = models.CharField(max_length=120)

    def __str__(self):
        return self.name, self.department, self.salary
