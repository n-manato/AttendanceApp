# Generated by Django 4.2 on 2023-04-28 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ATbook', '0005_remove_attend_hour_1_remove_attend_hour_2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='teacher',
            name='period',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_period', to='ATbook.period'),
        ),
    ]