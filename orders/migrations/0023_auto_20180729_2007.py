# Generated by Django 2.0.7 on 2018-07-30 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0022_auto_20180729_2001'),
    ]

    operations = [
        migrations.DeleteModel(
            name='pastaType',
        ),
        migrations.DeleteModel(
            name='pizzaType',
        ),
        migrations.DeleteModel(
            name='platterType',
        ),
        migrations.DeleteModel(
            name='saladType',
        ),
        migrations.DeleteModel(
            name='subType',
        ),
        migrations.DeleteModel(
            name='topping',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='item',
            field=models.CharField(default='Pizza', max_length=64),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='size',
            field=models.CharField(default='Small', max_length=64),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='special',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='toppings',
            field=models.IntegerField(default=0),
        ),
    ]
