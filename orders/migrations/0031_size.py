# Generated by Django 2.0.7 on 2018-07-31 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0030_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=64)),
            ],
        ),
    ]
