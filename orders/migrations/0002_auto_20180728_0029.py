# Generated by Django 2.0.7 on 2018-07-28 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='Pizza',
        ),
        migrations.RenameField(
            model_name='pizza',
            old_name='kindOfPizza',
            new_name='kind',
        ),
        migrations.RenameField(
            model_name='pizza',
            old_name='menuItem',
            new_name='special',
        ),
    ]
