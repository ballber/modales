# Generated by Django 3.0.2 on 2020-01-30 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_auto_20200130_0326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='descripcion',
            new_name='attribute',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='marca',
            new_name='crop1',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='precio',
            new_name='crop2',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='estado',
            new_name='crop3',
        ),
    ]