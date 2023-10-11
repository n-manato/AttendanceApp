# Generated by Django 4.2 on 2023-04-28 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ATbook', '0004_rename_kind_attend_hour_1_attend_hour_2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attend',
            name='hour_1',
        ),
        migrations.RemoveField(
            model_name='attend',
            name='hour_2',
        ),
        migrations.RemoveField(
            model_name='attend',
            name='hour_3',
        ),
        migrations.RemoveField(
            model_name='attend',
            name='hour_4',
        ),
        migrations.RemoveField(
            model_name='attend',
            name='hour_5',
        ),
        migrations.RemoveField(
            model_name='attend',
            name='hour_6',
        ),
        migrations.RemoveField(
            model_name='attend',
            name='hour_7',
        ),
        migrations.RemoveField(
            model_name='attend',
            name='hour_8',
        ),
        migrations.AddField(
            model_name='attend',
            name='kind',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.CreateModel(
            name='HourAttend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour_1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_hour_1', to='ATbook.attend')),
                ('hour_2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_hour_2', to='ATbook.attend')),
                ('hour_3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_hour_3', to='ATbook.attend')),
                ('hour_4', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_hour_4', to='ATbook.attend')),
                ('hour_5', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_hour_5', to='ATbook.attend')),
                ('hour_6', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_hour_6', to='ATbook.attend')),
                ('hour_7', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_hour_7', to='ATbook.attend')),
                ('hour_8', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_hour_8', to='ATbook.attend')),
                ('hr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_hr', to='ATbook.attend')),
            ],
        ),
        migrations.AlterField(
            model_name='attendanceinfo',
            name='attendance',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_attendance', to='ATbook.hourattend'),
        ),
    ]