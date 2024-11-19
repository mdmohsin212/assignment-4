# Generated by Django 5.1.1 on 2024-11-19 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='taskTitle',
            field=models.CharField(max_length=100),
        ),
    ]
