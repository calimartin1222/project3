# Generated by Django 2.0.7 on 2018-07-30 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0026_auto_20180729_2012'),
    ]

    operations = [
        migrations.CreateModel(
            name='topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=64)),
            ],
        ),
    ]
