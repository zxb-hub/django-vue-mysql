# Generated by Django 2.1.4 on 2020-06-15 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20200615_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertoken',
            name='token',
            field=models.CharField(db_column='token', max_length=300),
        ),
    ]