# Generated by Django 4.2 on 2023-04-08 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("epilepsy12", "0077_auto_20230408_2041"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comorbidity",
            name="comorbidity_diagnosis",
        ),
        migrations.RemoveField(
            model_name="historicalcomorbidity",
            name="comorbidity_diagnosis",
        ),
        migrations.AlterField(
            model_name="comorbidity",
            name="comorbidity",
            field=models.ForeignKey(
                default=None,
                help_text={
                    "label": "What is the comorbidity?",
                    "reference": "What is the comorbidity?",
                },
                on_delete=django.db.models.deletion.CASCADE,
                to="epilepsy12.comorbidityentity",
            ),
        ),
        migrations.AlterField(
            model_name="historicalcomorbidity",
            name="comorbidity",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                default=None,
                help_text={
                    "label": "What is the comorbidity?",
                    "reference": "What is the comorbidity?",
                },
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="epilepsy12.comorbidityentity",
            ),
        ),
    ]