# Generated by Django 2.0.6 on 2018-12-28 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20181228_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='category',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
