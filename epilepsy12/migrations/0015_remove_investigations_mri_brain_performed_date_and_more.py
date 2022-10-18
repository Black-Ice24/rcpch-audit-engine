# Generated by Django 4.1.2 on 2022-10-18 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epilepsy12', '0014_remove_episode_were_any_of_the_epileptic_seizures_convulsive_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investigations',
            name='mri_brain_performed_date',
        ),
        migrations.AddField(
            model_name='investigations',
            name='mri_brain_reported_date',
            field=models.DateField(blank=True, default=None, help_text={
                                   'label': 'Date MRI brain reported', 'reference': 'Date MRI brain reported'}, null=True),
        ),
        migrations.AlterField(
            model_name='investigations',
            name='ct_head_scan_status',
            field=models.BooleanField(blank=True, default=None, help_text={
                                      'label': 'Has a CT head been performed?', 'reference': 'NICE states if MRI is contraindicated, consider a CT scan for children, young people and adults with epilepsy.'}, null=True),
        ),
        migrations.AlterField(
            model_name='investigations',
            name='eeg_indicated',
            field=models.BooleanField(blank=True, default=None, help_text={
                                      'label': 'Has a first EEG been requested?', 'reference': 'All children with Epilepsy should have an EEG'}, null=True),
        ),
        migrations.AlterField(
            model_name='investigations',
            name='mri_indicated',
            field=models.BooleanField(blank=True, default=None, help_text={
                                      'label': 'Has a brain MRI been requested?', 'reference': 'NICE recommends that an MRI scan should be offered to children, young people and adults diagnosed with epilepsy, unless they have idiopathic generalised epilepsy or self-limited epilepsy with centrotemporal spikes. The MRI should be carried out within 6 weeks of the MRI referral.'}, null=True),
        ),
        migrations.AlterField(
            model_name='investigations',
            name='twelve_lead_ecg_status',
            field=models.BooleanField(blank=True, default=None, help_text={
                                      'label': 'Has a 12-Lead ECG been performed?', 'reference': 'The Epilepsy12 standard is that all children with an convulsive episode should have a 12 lead ECG'}, null=True),
        ),
    ]
