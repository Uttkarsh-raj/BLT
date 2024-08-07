# Generated by Django 5.0.7 on 2024-08-04 23:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0120_suggestion_suggestionvotes"),
    ]

    operations = [
        migrations.AddField(
            model_name="ip",
            name="count",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="ip",
            name="method",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="ip",
            name="path",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="ip",
            name="referer",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="ip",
            name="user_agent_string",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="ip",
            name="address",
            field=models.CharField(blank=True, max_length=39, null=True),
        ),
        migrations.AlterField(
            model_name="ip",
            name="user",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
