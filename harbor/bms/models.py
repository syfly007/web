from __future__ import unicode_literals

from django.db import models


class Harbor(models.Model):
    place = models.CharField(max_length=30)
    throughput = models.IntegerField()


class Person(models.Model):
    Harbor = models.ForeignKey(Harbor, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    tel_num = models.CharField(max_length=14)
    kind = (
        ('AD', 'Admin'),
        ('HB', 'HarborOwn'),
        ('CT', 'Customer'),
    )


class Order(models.Model):
    Harbor = models.ForeignKey(Harbor, on_delete=models.CASCADE)
    kind = (
        ('IN', 'Enter Harbor'),
        ('OUT', 'Leave Harbor'),
    )
    price = models.IntegerField() #??
    