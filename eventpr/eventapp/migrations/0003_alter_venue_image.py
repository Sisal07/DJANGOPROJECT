# Generated by Django 5.0.6 on 2024-06-12 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0002_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='image',
            field=models.ImageField(upload_to='pic/'),
        ),
    ]
