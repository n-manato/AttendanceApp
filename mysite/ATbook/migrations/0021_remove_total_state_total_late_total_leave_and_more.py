# Generated by Django 4.2 on 2023-10-12 02:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ATbook", "0020_status_total"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="total",
            name="state",
        ),
        migrations.AddField(
            model_name="total",
            name="late",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name="total",
            name="leave",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.DeleteModel(
            name="Status",
        ),
    ]