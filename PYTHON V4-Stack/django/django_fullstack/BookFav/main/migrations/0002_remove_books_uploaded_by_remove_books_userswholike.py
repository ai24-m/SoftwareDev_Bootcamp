# Generated by Django 4.0.5 on 2022-06-24 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='uploaded_by',
        ),
        migrations.RemoveField(
            model_name='books',
            name='usersWhoLike',
        ),
    ]