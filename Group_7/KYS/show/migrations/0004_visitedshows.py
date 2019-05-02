# Generated by Django 2.1.2 on 2019-05-01 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0003_show_movieviewcount'),
    ]

    operations = [
        migrations.CreateModel(
            name='visitedShows',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitedShows', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='show.Show')),
            ],
        ),
    ]