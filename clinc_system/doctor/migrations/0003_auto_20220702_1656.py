# Generated by Django 3.2.3 on 2022-07-02 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_auto_20220702_1655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine_items',
            name='featured',
        ),
        migrations.RemoveField(
            model_name='roshetta',
            name='featured',
        ),
    ]