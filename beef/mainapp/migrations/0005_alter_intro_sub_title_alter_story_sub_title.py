# Generated by Django 5.0.6 on 2024-06-30 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_story'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intro',
            name='sub_title',
            field=models.TextField(default='text'),
        ),
        migrations.AlterField(
            model_name='story',
            name='sub_title',
            field=models.TextField(default='text'),
        ),
    ]
