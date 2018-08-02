# Generated by Django 2.0.7 on 2018-08-02 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0031_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('item_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='item',
        ),
        migrations.DeleteModel(
            name='size',
        ),
    ]