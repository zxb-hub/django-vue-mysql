# Generated by Django 3.0.2 on 2020-01-22 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200122_1552'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-publishDate']},
        ),
    ]
