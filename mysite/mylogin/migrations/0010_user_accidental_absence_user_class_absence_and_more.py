# Generated by Django 4.2 on 2023-09-26 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylogin', '0009_subject_number_of_classes'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='accidental_absence',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='class_absence',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='leaving_early',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='sick_absence',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='tardiness',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
