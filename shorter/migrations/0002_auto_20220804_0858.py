# Generated by Django 3.1.4 on 2022-08-04 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorter', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shortener',
            options={'ordering': ['-created_at']},
        ),
        migrations.RenameField(
            model_name='shortener',
            old_name='created',
            new_name='created_at',
        ),
        migrations.AlterField(
            model_name='shortener',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
