# Generated by Django 3.1.1 on 2020-09-30 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_item_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='owner',
        ),
    ]
