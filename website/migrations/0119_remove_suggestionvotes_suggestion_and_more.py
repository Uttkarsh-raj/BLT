# Generated by Django 5.0.7 on 2024-08-04 19:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0118_rename_date_created_contribution_created"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="suggestionvotes",
            name="suggestion",
        ),
        migrations.RemoveField(
            model_name="suggestionvotes",
            name="user",
        ),
        migrations.DeleteModel(
            name="Suggestion",
        ),
        migrations.DeleteModel(
            name="SuggestionVotes",
        ),
    ]
