# Generated by Django 3.2.13 on 2022-05-29 21:25

import csv
from os.path import join

from django.conf import settings
from django.db import migrations


def add_initial_rackets(apps, schema_editor):
    Racket = apps.get_model("racket_stringer", "Racket")

    data_file = join(settings.BASE_DIR, "initial_data/rackets.csv")
    with open(data_file) as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            Racket.objects.get_or_create(**row)


def add_initial_strings(apps, schema_editor):
    String = apps.get_model("racket_stringer", "String")

    data_file = join(settings.BASE_DIR, "initial_data/strings.csv")
    with open(data_file) as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            String.objects.get_or_create(**row)


class Migration(migrations.Migration):

    dependencies = [
        ("racket_stringer", "0002_auto_20220515_2104"),
    ]

    operations = [
        migrations.RunPython(add_initial_rackets),
        migrations.RunPython(add_initial_strings),
    ]
