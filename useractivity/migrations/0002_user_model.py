# Generated by Django 3.0.8 on 2020-07-03 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useractivity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('real_name', models.CharField(max_length=30)),
                ('tz', models.CharField(max_length=30)),
            ],
        ),
    ]
