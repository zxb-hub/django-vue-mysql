# Generated by Django 2.1.5 on 2019-08-21 07:00

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_column='username', max_length=20)),
                ('password', models.CharField(db_column='password', max_length=20)),
                ('sex', models.BooleanField(db_column='sex')),
                ('last_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'users',
                'ordering': ['username'],
            },
            managers=[
                ('userM', django.db.models.manager.Manager()),
            ],
        ),
    ]
