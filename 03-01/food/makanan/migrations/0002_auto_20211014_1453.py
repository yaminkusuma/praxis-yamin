# Generated by Django 3.2.8 on 2021-10-14 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makanan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='makanan',
            name='harga',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='makanan',
            name='nama',
            field=models.TextField(default=''),
        ),
    ]