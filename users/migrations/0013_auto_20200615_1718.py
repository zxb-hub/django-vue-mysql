# Generated by Django 2.1.4 on 2020-06-15 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20200615_1048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usertoken',
            old_name='uid',
            new_name='username',
        ),
    ]
