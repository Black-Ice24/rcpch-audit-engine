# Generated by Django 4.1.2 on 2022-10-20 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epilepsy12', '0015_remove_investigations_mri_brain_performed_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='referring_clinician',
        ),
        migrations.AlterField(
            model_name='management',
            name='has_an_aed_been_given',
            field=models.BooleanField(blank=True, default=None, help_text={'label': 'Has an antiseizure medicine been given?', 'reference': 'Has an antiseizure medicine been given?'}, null=True),
        ),
        migrations.AlterField(
            model_name='management',
            name='has_individualised_care_plan_been_updated_in_the_last_year',
            field=models.BooleanField(blank=True, default=None, help_text={'label': 'Being updated as necessary', 'reference': 'Has the individualised care plan been updated in the last year?'}, null=True),
        ),
        migrations.AlterField(
            model_name='management',
            name='has_rescue_medication_been_prescribed',
            field=models.BooleanField(blank=True, default=None, help_text={'label': 'Has a rescue medicine been prescribed?', 'reference': 'Has a rescue medicine been prescribed?'}, null=True),
        ),
        migrations.AlterField(
            model_name='management',
            name='individualised_care_plan_addresses_sudep',
            field=models.BooleanField(blank=True, default=None, help_text={'label': 'Sudden unexplained death in epilepsy (SUDEP)', 'reference': 'Does the individualised care plan address sudden unexplained death in epilepsy?'}, null=True),
        ),
        migrations.AlterField(
            model_name='management',
            name='individualised_care_plan_addresses_water_safety',
            field=models.BooleanField(blank=True, default=None, help_text={'label': 'Water safety', 'reference': 'Does the individualised care plan address water safety?'}, null=True),
        ),
        migrations.AlterField(
            model_name='management',
            name='individualised_care_plan_date',
            field=models.DateField(blank=True, default=None, help_text={'label': 'On what date was the individualised care plan put in place?', 'reference': 'On what date was the individualised care plan put in place?'}, null=True),
        ),
        migrations.AlterField(
            model_name='management',
            name='individualised_care_plan_has_parent_carer_child_agreement',
            field=models.BooleanField(blank=True, default=None, help_text={'label': 'Parent or carer and child agreement', 'reference': 'Has the parent or carer and child agreement to an individualised care plan been documented?'}, null=True),
        ),
        migrations.AlterField(
            model_name='management',
            name='individualised_care_plan_in_place',
            field=models.BooleanField(blank=True, default=None, help_text={'label': 'Has care planning (either an individualised epilepsy document or copy clinic letter including care planning information) commenced?', 'reference': 'Has care planning (either an individualised epilepsy document or copy clinic letter including care planning information) commenced?'}, null=True),
        ),
        migrations.AlterField(
            model_name='management',
            name='individualised_care_plan_include_first_aid',
            field=models.BooleanField(blank=True, default=None, help_text={'label': 'First aid advice', 'reference': 'Does the individualised care plan include first aid advice?'}, null=True),
        ),
        migrations.AlterField(
            model_name='management',
            name='individualised_care_plan_includes_ehcp',
            field=models.BooleanField(blank=True, default=None, help_text={'label': 'An educational health care plan (EHCP)', 'reference': 'Does the individualised care plan include an educational health care plan (EHCP)?'}, null=True),
        ),
        migrations.AlterField(
            model_name='management',
            name='individualised_care_plan_includes_general_participation_risk',
            field=models.BooleanField(blank=True, default=None, help_text={'label': 'General participation and risk assessment', 'reference': 'Does the individualised care plan include general participation and risk assessment?'}, null=True),
        ),
        migrations.AlterField(
            model_name='management',
            name='individualised_care_plan_includes_service_contact_details',
            field=models.BooleanField(blank=True, default=None, help_text={'label': 'Service contact details', 'reference': 'Does the individualised care plan include service contact details?'}, null=True),
        ),
        migrations.AlterField(
            model_name='management',
            name='individualised_care_plan_parental_prolonged_seizure_care',
            field=models.BooleanField(blank=True, default=None, help_text={'label': 'Parental advice on managing prolonged seizures', 'reference': 'Does the individualised care plan include parental advice on managing prolonged seizures?'}, null=True),
        ),
        migrations.AlterField(
            model_name='management',
            name='is_a_pregnancy_prevention_programme_in_place',
            field=models.BooleanField(blank=True, default=None, help_text={'label': 'Is there a pregnancy prevention programme (PPP) in place?', 'reference': 'Is there a pregnancy prevention programme (PPP) in place?'}, null=True),
        ),
    ]
