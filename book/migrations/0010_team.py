# Generated by Django 2.0.4 on 2018-04-27 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0009_auto_20180427_0920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('logo', models.ImageField(unique=True, upload_to='')),
            ],
        ),
    ]
