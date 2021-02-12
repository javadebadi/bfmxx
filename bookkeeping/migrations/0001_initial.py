# Generated by Django 3.1.6 on 2021-02-12 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('account_type', models.CharField(choices=[('AS', 'Assets'), ('LB', 'Liability'), ('CP', 'Capital'), ('IN', 'Income'), ('EX', 'Expense')], default='AS', max_length=2)),
                ('account_name', models.CharField(max_length=128, primary_key=True, serialize=False, unique=True)),
                ('account_description', models.CharField(blank=True, default='a new account', max_length=255)),
                ('account_category', models.CharField(blank=True, choices=[('AS/FX', 'Fixed Asset'), ('AS/CR', 'Current Asset')], max_length=9, null=True)),
            ],
        ),
    ]
