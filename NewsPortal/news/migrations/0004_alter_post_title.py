# Generated by Django 5.0.7 on 2025-03-07 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_rename_categories_post_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=55),
        ),
    ]
