# Generated by Django 2.0.7 on 2018-07-30 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0027_topping'),
    ]

    operations = [
        migrations.AddField(
            model_name='topping',
            name='item',
            field=models.CharField(default='Pizza', max_length=64),
        ),
    ]
