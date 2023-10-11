# Generated by Django 4.2 on 2023-06-30 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mylogin', '0002_hour_period_subject_user_subject'),
        ('ATbook', '0012_subject_department_f'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='Department_f',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='hour_f',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='period_f',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='teacher_f',
        ),
        migrations.RemoveField(
            model_name='attendanceinfo',
            name='subject',
        ),
        migrations.AddField(
            model_name='attendanceinfo',
            name='subject_f',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_subject', to='mylogin.subject'),
        ),
        migrations.AlterField(
            model_name='attendanceinfo',
            name='time',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_hourattend', to='mylogin.hour'),
        ),
        migrations.DeleteModel(
            name='Hour',
        ),
        migrations.DeleteModel(
            name='Period',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
