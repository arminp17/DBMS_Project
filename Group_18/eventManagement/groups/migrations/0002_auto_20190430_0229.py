# Generated by Django 2.1.7 on 2019-04-30 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group_invite',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]