# Generated by Django 3.2.2 on 2023-09-23 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0002_receipe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipe',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
