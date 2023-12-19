from django.db import models

# Create your models here.

class customer(models.Model):
    name=models.CharField(max_length=50)
    Address=models.CharField(max_length=50)
    City=models.CharField(max_length=50)
    phone=models.IntegerField(null=True)
    Email=models.EmailField()
    def __str__(self):
        return self.name
