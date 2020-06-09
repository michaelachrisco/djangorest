from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)


class Transaction(models.Model):
    amount = models.DecimalField(decimal_places=2, default=0.00, max_digits=7)
    action_datetime = models.DateField()
    note = models.CharField(max_length=30)
