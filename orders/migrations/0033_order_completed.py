# Generated by Django 2.0.7 on 2018-08-02 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0032_auto_20180801_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
