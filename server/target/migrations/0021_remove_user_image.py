# Generated by Django 4.0.3 on 2022-03-13 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('target', '0020_alter_jobseeker_resume'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
    ]
