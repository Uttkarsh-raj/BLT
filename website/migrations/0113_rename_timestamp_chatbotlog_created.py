# Generated by Django 5.0.7 on 2024-08-04 18:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0112_rename_created_at_transaction_created_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="chatbotlog",
            old_name="timestamp",
            new_name="created",
        ),
    ]
