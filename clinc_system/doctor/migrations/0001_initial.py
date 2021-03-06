# Generated by Django 3.2.3 on 2022-07-01 19:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('Scientifc_Name', models.CharField(blank=True, max_length=250)),
                ('type', models.CharField(blank=True, max_length=250)),
                ('description', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Diseases',
            },
        ),
        migrations.CreateModel(
            name='Medcine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('Generic_Name', models.CharField(blank=True, max_length=250)),
                ('type', models.CharField(blank=True, max_length=250)),
                ('price', models.FloatField(default=0)),
                ('stock', models.IntegerField()),
                ('description', models.TextField(blank=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Medcines',
            },
        ),
        migrations.CreateModel(
            name='Testing_API',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'APIs',
            },
        ),
        migrations.CreateModel(
            name='Roshetta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('featured', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('disease', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='doctor.disease')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Roshettas',
            },
        ),
        migrations.CreateModel(
            name='Medicine_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('featured', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('medicine', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='doctor.medcine')),
                ('roshetta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='doctor.roshetta')),
            ],
            options={
                'verbose_name_plural': 'Medicines_items',
            },
        ),
    ]
