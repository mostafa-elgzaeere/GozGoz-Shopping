# Generated by Django 3.2.2 on 2021-05-11 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='avilable',
            field=models.BooleanField(default=True),
        ),
    ]
