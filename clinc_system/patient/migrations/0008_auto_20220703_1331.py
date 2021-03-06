# Generated by Django 3.2.3 on 2022-07-03 11:31

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0007_alter_appointment_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Are_you_deaf',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Question_02',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Question_03',
        ),
        migrations.AddField(
            model_name='profile',
            name='Do_you_suffer_from',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Parks of being a wallflower', 'Parks of being a wallflower'), ('All the bright places', 'All the bright places'), ('The girl on the train', 'The girl on the train'), ('Django', 'Django')], default=12, max_length=78),
            preserve_default=False,
        ),
    ]
