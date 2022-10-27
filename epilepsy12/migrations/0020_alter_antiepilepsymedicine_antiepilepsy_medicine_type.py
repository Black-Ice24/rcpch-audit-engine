# Generated by Django 4.1.2 on 2022-10-23 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epilepsy12', '0019_remove_management_is_a_pregnancy_prevention_programme_in_place_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antiepilepsymedicine',
            name='antiepilepsy_medicine_type',
            field=models.IntegerField(blank=True, choices=[(5, 'Eslicarbazepine acetate'), (9, 'Levetiracetam'), (16, 'Phenytoin'), (15, 'Phenobarbital'), (28, 'Epidyolex® '), (17, 'Pregabalin'), (1, 'ACTH'), (13, 'Perampanel'), (7, 'Lacosamide'), (0, 'Acetazolamide'), (6, 'Ethosuximide;Gabapentin'), (8, 'Lamotrigine'), (22, 'Stiripentol'), (25, 'Topiramate'), (14, 'Piracetam'), (19, 'Primidone'), (24, 'Tiagabine'), (3, 'Clobazam'), (18, 'Prednisolone'), (2, 'Carbamazepine'), (27, 'Zonisamide'), (23, 'Sulthiame'), (29, 'Other Cannabis-based medicinal product'), (11, 'Nitrazepam'), (21, 'Sodium valproate'), (4, 'Clonazepam'), (12, 'Oxcarbazepine'), (10, 'Methylprednisolone'), (30, 'Other'), (26, 'Vigabatrin'), (20, 'Rufinamide')], default=None, help_text={'label': 'Antiseizure medicine name', 'reference': 'Please enter antiseizure medicine name.'}, null=True),
        ),
    ]