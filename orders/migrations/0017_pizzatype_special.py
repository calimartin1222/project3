# Generated by Django 2.0.7 on 2018-07-30 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_pizzatype_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizzatype',
            name='special',
            field=models.BooleanField(default=True),
        ),
    ]
