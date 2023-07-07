# Generated by Django 4.2.2 on 2023-06-15 21:22

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "epilepsy12",
            "0013_alter_historicalorganisation_geocode_coordinates_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="epilepsy12user",
            name="bio",
        ),
        migrations.RemoveField(
            model_name="epilepsy12user",
            name="twitter_handle",
        ),
        migrations.RemoveField(
            model_name="historicalepilepsy12user",
            name="bio",
        ),
        migrations.RemoveField(
            model_name="historicalepilepsy12user",
            name="twitter_handle",
        ),
        migrations.AddField(
            model_name="epilepsy12user",
            name="is_clinician",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="epilepsy12user",
            name="is_patient_or_carer",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="historicalepilepsy12user",
            name="is_clinician",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="historicalepilepsy12user",
            name="is_patient_or_carer",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="historicalmultiaxialdiagnosis",
            name="global_developmental_delay_or_learning_difficulties_severity",
            field=models.CharField(
                blank=True,
                choices=[
                    ("mild", "Mild"),
                    ("moderate", "Moderate"),
                    ("severe", "Severe"),
                    ("profound", "Profound"),
                    ("uncertain", "Uncertain"),
                ],
                default=None,
                help_text={
                    "label": "Add details on the severity of the neurodevelopmental condition.",
                    "reference": "Add details on the severity of the neurodevelopmental condition.",
                },
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalorganisation",
            name="Geocode_Coordinates",
            field=django.contrib.gis.db.models.fields.PointField(
                blank=True, default=None, null=True, srid=27700
            ),
        ),
        migrations.AlterField(
            model_name="multiaxialdiagnosis",
            name="global_developmental_delay_or_learning_difficulties_severity",
            field=models.CharField(
                blank=True,
                choices=[
                    ("mild", "Mild"),
                    ("moderate", "Moderate"),
                    ("severe", "Severe"),
                    ("profound", "Profound"),
                    ("uncertain", "Uncertain"),
                ],
                default=None,
                help_text={
                    "label": "Add details on the severity of the neurodevelopmental condition.",
                    "reference": "Add details on the severity of the neurodevelopmental condition.",
                },
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="organisation",
            name="Geocode_Coordinates",
            field=django.contrib.gis.db.models.fields.PointField(
                blank=True, default=None, null=True, srid=27700
            ),
        ),
    ]
