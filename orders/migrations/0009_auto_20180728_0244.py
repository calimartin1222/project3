# Generated by Django 2.0.7 on 2018-07-28 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_pastatypes_plattertypes_saladtypes_sizes_subtypes_toppings'),
    ]

    operations = [
        migrations.DeleteModel(
            name='pastaTypes',
        ),
        migrations.DeleteModel(
            name='platterTypes',
        ),
        migrations.DeleteModel(
            name='saladTypes',
        ),
        migrations.DeleteModel(
            name='sizes',
        ),
        migrations.DeleteModel(
            name='subTypes',
        ),
        migrations.DeleteModel(
            name='toppings',
        ),
    ]
