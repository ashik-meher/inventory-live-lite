from django.db import models

# Create your models here.


class Entry(models.Model):
    productName = models.CharField(max_length=100)
    createdDate = models.DateTimeField(auto_now_add=True, null=True)
    quantity = models.FloatField(null=True)
    unit = models.CharField(max_length=20)
    price = models.IntegerField(null=True)
    pricePaid = models.IntegerField(null=True)
    dealer = models.CharField(max_length=30)
    receiver = models.CharField(max_length=30)
    remarks = models.TextField(max_length=200, null=True)
