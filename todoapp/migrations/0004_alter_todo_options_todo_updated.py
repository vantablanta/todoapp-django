# Generated by Django 4.0.4 on 2022-05-25 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['-created', '-updated']},
        ),
        migrations.AddField(
            model_name='todo',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]