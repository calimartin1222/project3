# Generated by Django 2.0.7 on 2018-07-28 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_delete_plattertype'),
    ]

    operations = [
        migrations.CreateModel(
            name='platterType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=64)),
                ('size', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
    ]
