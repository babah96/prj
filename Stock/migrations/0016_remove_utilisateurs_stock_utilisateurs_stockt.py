# Generated by Django 4.0 on 2022-01-28 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stock', '0015_utilisateurs_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utilisateurs',
            name='STOCK',
        ),
        migrations.AddField(
            model_name='utilisateurs',
            name='STOCKT',
            field=models.CharField(default=1, max_length=220),
            preserve_default=False,
        ),
    ]
