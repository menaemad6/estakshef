# Generated by Django 4.1.4 on 2022-12-18 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_rename_passw_newsite_passwords_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='first_image',
            field=models.ImageField(upload_to='', verbose_name='First Image (Main)'),
        ),
    ]