# Generated by Django 4.0.4 on 2022-07-31 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('epilepsy12', '0020_remove_site_site_site_hospital_trust_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='hospital_trust',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='hospital_site', to='epilepsy12.hospitaltrust'),
        ),
    ]
