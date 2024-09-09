from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    # pbb_class = models.CharField(max_length=1)
    # student_id = models.CharField(max_length=10)
    price = models.IntegerField() 
    description = models.TextField()