# Generated by Django 3.0.3 on 2020-03-22 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='news',
            name='published_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]