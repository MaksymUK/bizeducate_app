# Generated by Django 4.2.13 on 2025-05-31 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0007_rename_text_coursekeyquestion_question_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="courseaudience",
            name="audience",
            field=models.CharField(max_length=500),
        ),
    ]
