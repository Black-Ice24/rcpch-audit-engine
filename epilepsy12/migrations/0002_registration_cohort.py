# Generated by Django 4.0 on 2022-03-17 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epilepsy12', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='cohort',
            field=models.PositiveSmallIntegerField(default=None, null=True),
        ),
    ]
