# Generated by Django 5.0.2 on 2024-03-14 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='profile_image',
            new_name='user_profile_image',
        ),
    ]
