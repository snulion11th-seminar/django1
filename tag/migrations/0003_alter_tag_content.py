# Generated by Django 4.1.7 on 2023-05-24 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0002_alter_tag_content_alter_tag_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='content',
            field=models.TextField(),
        ),
    ]