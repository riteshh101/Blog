# Generated by Django 3.1.2 on 2021-01-03 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='uname',
            field=models.CharField(default=None, max_length=150),
        ),
    ]
