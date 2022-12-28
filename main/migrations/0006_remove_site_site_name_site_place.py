# Generated by Django 4.1.4 on 2022-12-14 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_site_first_image_alter_site_second_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='site',
            name='site_name',
        ),
        migrations.AddField(
            model_name='site',
            name='place',
            field=models.CharField(default=1, max_length=150, verbose_name='Site Place'),
            preserve_default=False,
        ),
    ]
