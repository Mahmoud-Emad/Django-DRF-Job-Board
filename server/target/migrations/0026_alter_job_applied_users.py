# Generated by Django 4.0.3 on 2022-03-14 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('target', '0025_alter_job_title_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='applied_users',
            field=models.ManyToManyField(blank=True, related_name='applied_users', to='target.jobseeker'),
        ),
    ]
