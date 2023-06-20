from django.db import models




class Bank(models.Model):
    ifsc = models.CharField(max_length=11)
    bank_id = models.IntegerField(null=False)
    branch = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=20)
