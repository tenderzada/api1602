# Generated by Django 3.1.4 on 2021-01-28 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nano', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspost',
            name='avator',
            field=models.ImageField(blank=True, upload_to='news/%Y%m%d/'),
        ),
    ]
