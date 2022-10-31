# Generated by Django 4.1.2 on 2022-10-29 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epilepsy12', '0029_rename_initialassessment_firstpaediatricassessment_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='multiaxialdiagnosis',
            options={'verbose_name': 'Multiaxial Diagnosis', 'verbose_name_plural': 'Multiaxial diagnosis assessments'},
        ),
        migrations.RemoveField(
            model_name='episode',
            name='has_number_of_episodes_since_the_first_been_documented',
        ),
        migrations.AlterField(
            model_name='episode',
            name='epileptic_generalised_onset',
            field=models.CharField(blank=True, choices=[('AEM', 'Absence with eyelid myoclonia'), ('Aab', 'Atypical absence'), ('Ato', 'Atonic'), ('Clo', 'Clonic'), ('EpS', 'Epileptic spasms'), ('MAb', 'Myoclonic absence'), ('MAt', 'Myoclonic-atonic'), ('MTC', 'Myoclonic-tonic-clonic'), ('MyC', 'Myoclonic'), ('Oth', 'Other'), ('TAb', 'Typical absence'), ('TCl', 'Tonic-clonic'), ('Ton', 'Tonic')], default=None, help_text={'label': 'How best describes the generalised nature of the epileptic episode(s)?', 'reference': 'How best describes the generalised nature of the epileptic episode(s)?'}, max_length=3, null=True),
        ),
    ]