# Generated by Django 4.1.7 on 2023-03-27 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
