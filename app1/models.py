from django.db import models

class Laptop(models.Model):
    laptop_id = models.IntegerField(unique=True)
    model_name = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    ram = models.IntegerField()
    processor = models.CharField(max_length=20)
    price = models.IntegerField()

