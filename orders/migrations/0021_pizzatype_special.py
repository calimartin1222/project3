# Generated by Django 2.0.7 on 2018-07-30 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0020_remove_pizzatype_special'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizzatype',
            name='special',
            field=models.BooleanField(default=False),
        ),
    ]
