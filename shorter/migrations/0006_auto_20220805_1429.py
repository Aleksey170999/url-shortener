# Generated by Django 3.1.4 on 2022-08-05 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorter', '0005_remove_url_ckicks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='times_followed',
            field=models.IntegerField(default=0),
        ),
    ]
