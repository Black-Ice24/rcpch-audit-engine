# Generated by Django 4.2 on 2023-04-24 14:33

# Python
from datetime import date
from random import randint, choice

# Third-party Imports
from django.db import migrations

# RCPCH Imports
from ..models import Case, Organisation, Site
from ..constants import DUMMY_NAMES, ETHNICITIES
from ..general_functions import random_postcodes

def seed_dummy_cases(apps, schema_editor):
    """
    This function generates random dummy cases and saves them to the database.
    Postcodes are generated using postcodes.io.
    Organisations are chosen at random from the list of available organisations.
    For each case, a site is created with the chosen organisation and is linked to the case.
    """

    print('\033[33m', 'Seeding fictional cases...', '\033[33m')
    # there should not be any cases yet, but sometimes seed gets run more than once
    # if Case.objects.all().exists():
    #     print('Cases already exist. Skipping this step...')
    #     return

    postcode_list = random_postcodes.generate_postcodes(requested_number=100)

    random_organisations = []

    # first populate Addenbrooke's for ease of dev testing
    for _ in range(1, 11):
        random_organisations.append(
            Organisation.objects.get(ODSCode='RGT01'))

    # seed the remaining 9
    for j in range(9):
        random_organisation = Organisation.objects.order_by("?").first()
        for i in range(1, 11):
            random_organisations.append(random_organisation)

    for index in range(len(DUMMY_NAMES) - 1):
        random_date = date(randint(2005, 2021), randint(1, 12), randint(1, 28))
        nhs_number = randint(1000000000, 9999999999)
        first_name = DUMMY_NAMES[index]['firstname']
        surname = DUMMY_NAMES[index]['lastname']
        gender_object = DUMMY_NAMES[index]['gender']
        if gender_object == 'm':
            sex = 1
        else:
            sex = 2
        date_of_birth = random_date
        postcode = postcode_list[index]
        ethnicity = choice(ETHNICITIES)[0]

        # get a random organisation
        organisation = random_organisations[index]

        case_has_error = False

        try:
            new_case = Case(
                locked=False,
                nhs_number=nhs_number,
                first_name=first_name,
                surname=surname,
                sex=sex,
                date_of_birth=date_of_birth,
                postcode=postcode,
                ethnicity=ethnicity
            )
            new_case.save()
        except Exception as e:
            print(f"Error saving case: {e}")
            case_has_error = True

        if not case_has_error:
            try:
                new_site = Site.objects.create(
                    organisation=organisation,
                    site_is_actively_involved_in_epilepsy_care=True,
                    site_is_primary_centre_of_epilepsy_care=True,
                    case=new_case
                )
                new_site.save()
            except Exception as e:
                print(f"Error saving site: {e}")

            print(
                f"{new_case.first_name} {new_case.surname} at {new_site.organisation.OrganisationName} ({new_site.organisation.ParentOrganisation_OrganisationName})...")
    print(f"Saved {index} cases.")


class Migration(migrations.Migration):
    dependencies = [
        ("epilepsy12", "0008_seed_medicines"),
    ]

    operations = [migrations.RunPython(seed_dummy_cases)]