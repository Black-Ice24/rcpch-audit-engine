# Generated by Django 4.2 on 2023-04-08 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("epilepsy12", "0068_alter_historicalsyndromeentity_syndrome_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalsyndrome",
            name="syndrome",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                default=None,
                help_text={
                    "label": "The date the syndrome diagnosis was made.",
                    "reference": "The date the syndrome diagnosis was made.",
                },
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="epilepsy12.syndromeentity",
            ),
        ),
        migrations.AlterField(
            model_name="syndrome",
            name="syndrome",
            field=models.ForeignKey(
                blank=True,
                default=None,
                help_text={
                    "label": "The date the syndrome diagnosis was made.",
                    "reference": "The date the syndrome diagnosis was made.",
                },
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="epilepsy12.syndromeentity",
            ),
        ),
    ]