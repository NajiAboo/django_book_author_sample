# Generated by Django 3.2.6 on 2022-01-15 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0002_auto_20220111_0411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.IntegerField(),
        ),
    ]
