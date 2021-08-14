# Generated by Django 3.2.2 on 2021-05-11 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('price', models.DecimalField(db_index=True, decimal_places=2, max_digits=5)),
                ('description', models.TextField(blank=True, max_length=400, null=True)),
                ('image', models.ImageField(upload_to='static\\img')),
                ('slug', models.SlugField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('categorey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.categorey')),
            ],
        ),
    ]