# Generated by Django 3.2.3 on 2022-07-02 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0006_alter_appointment_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
    ]
