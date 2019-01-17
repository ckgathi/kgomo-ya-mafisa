from django.db import models

from .address import Address


class Payment(models.Model):

    amount = models.DecimalField(max_length=200)

    lastname = models.CharField(max_length=200)

    join_date = models.DateTimeField('Join Date')

    omang = models.CharField(max_length=200)

    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    left_date = models.DateTimeField('Left Date')
