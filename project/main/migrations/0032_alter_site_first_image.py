# Generated by Django 4.1.4 on 2022-12-18 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_alter_site_first_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='first_image',
            field=models.ImageField(upload_to='newfolder/', verbose_name='First Image (Main)'),
        ),
    ]
