# Generated by Django 4.2.9 on 2024-02-11 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_remove_author_company_remove_author_company_logo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testimonial',
            old_name='author',
            new_name='owner',
        ),
    ]