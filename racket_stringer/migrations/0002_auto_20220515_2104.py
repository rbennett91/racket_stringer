# Generated by Django 3.2.13 on 2022-05-16 01:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racket_stringer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['due_date']},
        ),
        migrations.AddField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='order',
            name='cross_string_tension',
            field=models.PositiveSmallIntegerField(blank=True, default=50, null=True, validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='order',
            name='main_string_tension',
            field=models.PositiveSmallIntegerField(blank=True, default=50, null=True, validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(20)]),
        ),
        migrations.AlterField(
            model_name='racket',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='string',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]