# Generated by Django 3.2.13 on 2023-03-26 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celery_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdatamodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
