# Generated by Django 3.2.3 on 2022-07-02 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0005_rename_question_01_profile_are_you_deaf'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'verbose_name_plural': 'Appointments'},
        ),
    ]