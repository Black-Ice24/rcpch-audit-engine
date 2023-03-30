# Generated by Django 4.1.7 on 2023-03-29 11:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "epilepsy12",
            "0060_alter_epilepsycontext_experienced_prolonged_focal_seizures_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="case",
            name="ethnicity",
            field=models.CharField(
                blank=True,
                choices=[
                    ("N", "African"),
                    ("L", "Any other Asian background"),
                    ("P", "Any other Black background"),
                    ("S", "Any other ethnic group"),
                    ("G", "Any other mixed background"),
                    ("C", "Any other White background"),
                    ("K", "Bangladeshi or British Bangladeshi"),
                    ("A", "British, Mixed British"),
                    ("M", "Caribbean"),
                    ("R", "Chinese"),
                    ("H", "Indian or British Indian"),
                    ("B", "Irish"),
                    ("Z", "Not Stated"),
                    ("J", "Pakistani or British Pakistani"),
                    ("F", "Mixed (White and Asian)"),
                    ("E", "Mixed (White and Black African)"),
                    ("D", "Mixed (White and Black Caribbean)"),
                ],
                max_length=4,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalcase",
            name="ethnicity",
            field=models.CharField(
                blank=True,
                choices=[
                    ("N", "African"),
                    ("L", "Any other Asian background"),
                    ("P", "Any other Black background"),
                    ("S", "Any other ethnic group"),
                    ("G", "Any other mixed background"),
                    ("C", "Any other White background"),
                    ("K", "Bangladeshi or British Bangladeshi"),
                    ("A", "British, Mixed British"),
                    ("M", "Caribbean"),
                    ("R", "Chinese"),
                    ("H", "Indian or British Indian"),
                    ("B", "Irish"),
                    ("Z", "Not Stated"),
                    ("J", "Pakistani or British Pakistani"),
                    ("F", "Mixed (White and Asian)"),
                    ("E", "Mixed (White and Black African)"),
                    ("D", "Mixed (White and Black Caribbean)"),
                ],
                max_length=4,
                null=True,
            ),
        ),
    ]