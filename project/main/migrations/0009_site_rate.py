# Generated by Django 4.1.4 on 2022-12-16 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_site_site_name_alter_site_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='rate',
            field=models.IntegerField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]