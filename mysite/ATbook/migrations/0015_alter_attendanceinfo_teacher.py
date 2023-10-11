# Generated by Django 4.2 on 2023-06-30 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ATbook', '0014_rename_subject_f_attendanceinfo_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendanceinfo',
            name='teacher',
            field=models.ForeignKey(limit_choices_to={'departments': 'student'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_teacher', to=settings.AUTH_USER_MODEL),
        ),
    ]
