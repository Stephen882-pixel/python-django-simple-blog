# Generated by Django 5.1.3 on 2024-11-19 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Meru University Blog Site', max_length=255),
        ),
    ]
