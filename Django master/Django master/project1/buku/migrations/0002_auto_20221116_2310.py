# Generated by Django 2.2 on 2022-11-17 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buku', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='judul',
            field=models.CharField(max_length=250),
        ),
    ]
