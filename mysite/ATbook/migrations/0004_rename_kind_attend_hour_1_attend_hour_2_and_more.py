# Generated by Django 4.2 on 2023-04-28 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ATbook', '0003_alter_attendanceinfo_attendance_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attend',
            old_name='kind',
            new_name='hour_1',
        ),
        migrations.AddField(
            model_name='attend',
            name='hour_2',
            field=models.CharField(default='present', max_length=50),
        ),
        migrations.AddField(
            model_name='attend',
            name='hour_3',
            field=models.CharField(default='present', max_length=50),
        ),
        migrations.AddField(
            model_name='attend',
            name='hour_4',
            field=models.CharField(default='present', max_length=50),
        ),
        migrations.AddField(
            model_name='attend',
            name='hour_5',
            field=models.CharField(default='present', max_length=50),
        ),
        migrations.AddField(
            model_name='attend',
            name='hour_6',
            field=models.CharField(default='present', max_length=50),
        ),
        migrations.AddField(
            model_name='attend',
            name='hour_7',
            field=models.CharField(default='present', max_length=50),
        ),
        migrations.AddField(
            model_name='attend',
            name='hour_8',
            field=models.CharField(default='present', max_length=50),
        ),
    ]
