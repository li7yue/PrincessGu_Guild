# Generated by Django 3.1.1 on 2020-10-02 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='required_dmg',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
