# Generated by Django 4.1.3 on 2023-03-09 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ai_images',
            name='ai_image',
            field=models.ImageField(max_length=200, upload_to='media/'),
        ),
    ]
