# Generated by Django 5.0.4 on 2024-05-30 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0002_remove_profile_profile_picture_profile_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('user', 'User'), ('instructor', 'Instructor')], default='user', max_length=20),
        ),
    ]
