from django.db import models

BOX_TYPE = (
    ('p.o.box', 'P. O. BOX'),
    ('private_bag', 'Private Bag'))


class Address(models.Model):

    box_typr = models.CharField(max_length=200, choices=BOX_TYPE)

    box_number = models.IntegerField(max_length=200)

    cyty = models.CharField(max_length=200)

    country = models.CharField(max_length=200)
