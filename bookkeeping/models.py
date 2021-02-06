from django.db import models

# Create your models here.
class Account(models.Model):
    """
    the Account class describes a parent model table which all accounts will
    be its subclass. Any account can be considred to be one the following types:
        - Asset
        - Liability
        - Income
        - Expense
    """
    ASSET='AS'
    LIABILITY='LB'
    INCOME='IN'
    EXPENSE='EX'
    ACCOUNT_TYPE_CHOICES = [
        (ASSET, 'Assets'),
        (LIABILITY, 'Liability'),
        (INCOME, 'Income'),
        (EXPENSE, 'Expense')
    ]

    account_type = models.CharField(
        max_length=2,
        choices=ACCOUNT_TYPE_CHOICES,
        null=False,
        blank=False,
        default=ASSET
    )

    account_name = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        unique=True,
        primary_key=True
    )

    def isAsset(self):
        return True if (account_type == ASSET) else False

    def isLiability(self):
        return True if (account_type == LIABILITY) else False
    
    def isIncome(self):
        return True if (account_type == INCOME) else False
    
    def isExpense(self):
        return True if (account_type == EXPENSE) else False

    def __str__(self):
        return f'{self.account_name} --- {self.account_type}'
    