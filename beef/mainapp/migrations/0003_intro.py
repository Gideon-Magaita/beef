# Generated by Django 5.0.6 on 2024-06-30 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_slider_sub_title_alter_slider_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('sub_title', models.TextField(blank=True, max_length=200, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='images')),
            ],
        ),
    ]
