# Generated by Django 4.0.5 on 2022-06-30 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_rename_created_date_link_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='identifier',
            field=models.SlugField(blank=True, max_length=20, unique=True),
        ),
    ]
