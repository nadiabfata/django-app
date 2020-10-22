from django.db import models

# Create your models here.
class Reserve(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    date = models.DateField()
    note = models.TextField()