# Generated by Django 4.1.3 on 2023-03-09 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AI_Images',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('desc', models.CharField(max_length=200)),
                ('ai_image', models.ImageField(max_length=200, upload_to='')),
            ],
        ),
    ]