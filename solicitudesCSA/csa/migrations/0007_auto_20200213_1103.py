# Generated by Django 3.0.2 on 2020-02-13 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csa', '0006_auto_20200213_1102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='csauser',
            old_name='area',
            new_name='area_id',
        ),
    ]
