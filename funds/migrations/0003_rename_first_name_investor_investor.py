# Generated by Django 4.1.7 on 2023-03-07 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0002_alter_investor_options_investor_fund_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='investor',
            old_name='first_name',
            new_name='investor',
        ),
    ]
