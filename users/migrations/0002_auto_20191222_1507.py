# Generated by Django 2.1.5 on 2019-12-22 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='sex',
        ),
        migrations.AddField(
            model_name='users',
            name='phone',
            field=models.CharField(db_column='phone', default=17855970276, max_length=30),
            preserve_default=False,
        ),
    ]