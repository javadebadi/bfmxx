import csv
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
        - Capital
    """
    ASSET='AS'
    LIABILITY='LB'
    CAPITAL="CP"
    INCOME='IN'
    EXPENSE='EX'
    ACCOUNT_TYPE_CHOICES = [
        (ASSET, 'Assets'),
        (LIABILITY, 'Liability'),
        (CAPITAL,'Capital'),
        (INCOME, 'Income'),
        (EXPENSE, 'Expense'),
    ]
    FIXED_ASSET = 'AS/FX'
    CURRENT_ASSET = 'AS/CR'
    ACCOUNT_CATEGORY_CHOICES = [
        (FIXED_ASSET, 'Fixed Asset'),
        (CURRENT_ASSET, 'Current Asset'),
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

    account_description = models.CharField(
        max_length=255,
        null=False,
        blank=True,
        default=f'a new account'
    )

    account_category = models.CharField(
        max_length=9,
        null=True,
        blank=True,
        choices=ACCOUNT_CATEGORY_CHOICES
    )

    def isAsset(self):
        return True if (self.account_type == self.ASSET) else False

    def isLiability(self):
        return True if (self.account_type == self.LIABILITY) else False
    
    def isIncome(self):
        return True if (self.account_type == self.INCOME) else False
    
    def isExpense(self):
        return True if (self.account_type == self.EXPENSE) else False

    def __str__(self):
        return f'{self.account_name} --- {self.account_type}'
    
    def fill_from_csv(self, file_path="bookkeeping/accounts.csv"):
        account = Account()
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                obj, created = Account.objects.get_or_create(
                    account_name = row['account_name'],
                    account_type = row['account_type'],
                    account_category = row['account_category'],
                    account_description = row['account_description'],
                )
                if created is False:
                    obj.save()