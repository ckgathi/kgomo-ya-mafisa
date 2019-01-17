from django.db import models

from .member import Member

ACCOUNT_TYPE = (
    ('member_accont', 'Member Account'),
    ('loan_account', 'Loan Account'))


class Account(models.Model):

    account_number = models.CharField(
        max_length=200,
        verbose_name='Account Number')

    balance = models.DecimalField(max_length=200)

    member = models.ForeignKey(Member, on_delete=models.CASCADE)


class MemberAccount(Account):

    charges = models.DecimalField(max_length=200)


class LoanAccount(models.Model):

    loan_amount = models.DecimalField(max_length=200)

    interest = models.DecimalField(max_length=200)

    amount_borrowed = models.DecimalField(max_length=200)

    total_amount_owed = models.DecimalField(max_length=200)
