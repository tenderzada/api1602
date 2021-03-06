# Generated by Django 3.1.5 on 2021-05-06 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('alertname', models.CharField(max_length=100)),
                ('instance', models.CharField(max_length=50)),
                ('anomaly_img', models.URLField()),
                ('startsAt', models.DateTimeField()),
                ('receiver', models.CharField(max_length=30)),
                ('longitude', models.CharField(max_length=30)),
                ('latitude', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'alert',
            },
        ),
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.CharField(max_length=30)),
                ('receiver_num', models.IntegerField()),
                ('dingtalk_robot_api', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'receiver',
                'unique_together': {('receiver', 'receiver_num')},
            },
        ),
    ]
