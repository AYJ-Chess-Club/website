# Generated by Django 3.2.4 on 2021-08-10 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_addannouncement_announcement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='difficulty',
            field=models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], max_length=225),
        ),
    ]
