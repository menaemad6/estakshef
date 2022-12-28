# Generated by Django 4.1.4 on 2022-12-26 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_remove_site_contact_remove_site_map_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True, unique=True, verbose_name='Site Slug (URL)'),
        ),
    ]