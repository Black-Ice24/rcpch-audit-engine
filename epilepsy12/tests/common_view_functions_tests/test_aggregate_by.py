"""Tests for aggregate_by.py functions.
"""

# python imports
import pytest
from datetime import date

# django imports

# E12 imports
from epilepsy12.common_view_functions import (
    cases_aggregated_by_sex,
    cases_aggregated_by_deprivation_score,
    cases_aggregated_by_ethnicity,
    aggregate_all_eligible_kpi_fields,
    all_registered_cases_for_cohort_and_abstraction_level,
    calculate_kpis,
)
from epilepsy12.models import (
    Organisation,
    Case,
    KPI,
    Registration,
    AntiEpilepsyMedicine,
)
from epilepsy12.constants import SEX_TYPE, DEPRIVATION_QUINTILES, ETHNICITIES


@pytest.mark.django_db
def test_cases_aggregated_by_sex_correct_output(e12_case_factory):
    """Tests the cases_aggregated_by_sex fn returns correct count."""

    # define constants
    ORGANISATION = Organisation.objects.first()

    # Create 10 cases of each available sex type
    for sex_type in SEX_TYPE:
        # set an organisation constant
        organisation = Organisation.objects.first()

        # For each sex, assign 10 cases
        for _ in range(10):
            e12_case_factory.create(
                sex=sex_type[0],
                registration=None,  # ensure related audit factories not generated
                organisations__organisation=ORGANISATION,
            )

    total_count = cases_aggregated_by_sex(selected_organisation=organisation).count()
    matching_count = (
        cases_aggregated_by_sex(selected_organisation=organisation)
        .filter(sexes=10)
        .count()
    )

    assert (
        total_count == matching_count
    ), f"Not returning correct count. {total_count} should equal {matching_count}"


@pytest.mark.django_db
def test_cases_aggregated_by_deprivation_score(e12_case_factory, e12_site_factory):
    """Tests the cases_aggregated_by_deprivation_score fn returns correct count."""

    # define constants
    ORGANISATION = Organisation.objects.first()

    # Loop through each ethnicity
    cases_list = []

    # Loop through each deprivation quintile
    for deprivation_type in DEPRIVATION_QUINTILES:
        # set an organisation constant
        organisation = Organisation.objects.first()

        # For each deprivation, assign 10 cases, add to cases_list
        for _ in range(10):
            case = e12_case_factory.build(
                index_of_multiple_deprivation_quintile=deprivation_type[1],
                registration=None,  # ensure related audit factories not generated
                organisations__organisation=ORGANISATION,
            )
            cases_list.append(case)

    # single SQL INSERT to save all cases
    Case.objects.bulk_create(cases_list)

    total_count = cases_aggregated_by_deprivation_score(
        selected_organisation=organisation
    ).count()

    matching_count = (
        cases_aggregated_by_deprivation_score(selected_organisation=organisation)
        .filter(cases_aggregated_by_deprivation=10)
        .count()
    )

    assert (
        total_count == matching_count
    ), f"Not returning correct count. {total_count=} should equal {matching_count=}"


@pytest.mark.django_db
def test_cases_aggregated_by_ethnicity(e12_case_factory):
    """Tests the cases_aggregated_by_ethnicity fn returns correct count."""

    # define constants
    ORGANISATION = Organisation.objects.first()

    # Loop through each ethnicity
    cases_list = []
    for ethnicity_type in ETHNICITIES:
        # For each ethnicity, build 10 cases, and append to cases_list
        for _ in range(10):
            case = e12_case_factory.build(
                ethnicity=ethnicity_type[0],
                registration=None,  # ensure related audit factories not generated
                organisations__organisation=ORGANISATION,
            )
            cases_list.append(case)

    # single SQL INSERT to save all cases
    Case.objects.bulk_create(cases_list)

    total_count = cases_aggregated_by_ethnicity(
        selected_organisation=ORGANISATION
    ).count()

    matching_count = (
        cases_aggregated_by_ethnicity(selected_organisation=ORGANISATION)
        .filter(ethnicities=10)
        .count()
    )

    assert (
        total_count == matching_count
    ), f"Not returning correct count. {total_count=} should equal {matching_count=}"


@pytest.mark.django_db
def test_aggregate_all_eligible_kpi_fields_correct_count(e12_case_factory):
    """Tests the aggregate_all_eligible_kpi_fields fn returns correct count of KPIs."""

    # define constants
    ORGANISATION = Organisation.objects.first()
    COHORT = 6

    for _ in range(10):
        e12_case_factory.create(organisations__organisation=ORGANISATION)

    organisation_level = all_registered_cases_for_cohort_and_abstraction_level(
        organisation_instance=ORGANISATION,
        cohort=COHORT,
        case_complete=False,
        abstraction_level="organisation",
    )

    aggregated_kpis = aggregate_all_eligible_kpi_fields(organisation_level)

    total_count_kpis = -1  # start at -1 to exclude "total_number_of_cases"
    for key in aggregated_kpis:
        if "total" in key:
            total_count_kpis += 1

    assert total_count_kpis == 21


@pytest.mark.django_db
def test_aggregate_all_eligible_kpi_fields_correct_kpi_scoring(e12_case_factory):
    """Tests the aggregate_all_eligible_kpi_fields fn returns scoring of KPIs."""

    # define constants
    ORGANISATION = Organisation.objects.first()

    pass_kpi_1 = {
        "registration__assessment__pass_paediatrician_with_expertise_in_epilepsies": True,
    }
    fail_kpi_1 = {
        "registration__assessment__fail_paediatrician_with_expertise_in_epilepsies": True
    }

    pass_kpi_2 = {
        "registration__assessment__pass_epilepsy_specialist_nurse": True,
    }
    fail_kpi_2 = {"registration__assessment__fail_epilepsy_specialist_nurse": True}

    eligible_kpi_3_5_ineligible_6_8_10 = {
        "eligible_kpi_3_5_ineligible_6_8_10": True,
    }
    eligible_kpi_6_8_10_ineligible_3_5 = {
        "eligible_kpi_6_8_10_ineligible_3_5": True,
        # extra ineligibility kpi 3
        "registration__assessment__ineligible_tertiary_input_AND_epilepsy_surgery_referral": True,
        # extra ineligibility kpi5
        "registration__ineligible_mri": True,
        "registration__multiaxial_diagnosis__ineligible_mri": True,
        "registration__multiaxial_diagnosis__syndrome_entity__ineligible_mri": True,
    }

    pass_kpi_3 = {
        "registration__assessment__pass_tertiary_input_AND_epilepsy_surgery_referral": True,
    }
    fail_kpi_3 = {
        "registration__assessment__fail_tertiary_input_AND_epilepsy_surgery_referral": True,
    }

    pass_kpi_4 = {
        "registration__epilepsy_context__pass_ecg": True,
        "registration__investigations__pass_ecg": True,
    }
    fail_kpi_4 = {
        "registration__epilepsy_context__fail_ecg": True,
        "registration__investigations__fail_ecg": True,
    }
    ineligible_kpi_4 = {
        "registration__epilepsy_context__ineligible_ecg": True,
    }

    pass_kpi_5 = {
        "registration__investigations__pass_mri": True,
    }
    fail_kpi_5 = {
        "registration__investigations__fail_mri": True,
    }

    pass_kpi_6 = {
        "pass_assessment_of_mental_health_issues": True,
        "registration__pass_assessment_of_mental_health_issues": True,
        "registration__multiaxial_diagnosis__pass_assessment_of_mental_health_issues": True,
    }
    fail_kpi_6 = {
        "fail_assessment_of_mental_health_issues": True,
        "registration__fail_assessment_of_mental_health_issues": True,
        "registration__multiaxial_diagnosis__fail_assessment_of_mental_health_issues": True,
    }

    pass_kpi_7 = {
        "registration__multiaxial_diagnosis__pass_mental_health_support": True,
        "registration__management__pass_mental_health_support": True,
    }
    fail_kpi_7 = {
        "registration__multiaxial_diagnosis__fail_mental_health_support": True,
        "registration__management__fail_mental_health_support": True,
    }
    ineligible_kpi_7 = {
        "registration__multiaxial_diagnosis__ineligible_mental_health_support": True,
    }

    pass_kpi_8 = {
        "pass_sodium_valproate": True,
        "registration__management__sodium_valproate": "pass",
    }
    fail_kpi_8 = {
        "fail_sodium_valproate": True,
        "registration__management__sodium_valproate": "fail",
    }

    pass_kpi_9 = {
        "registration__management__pass_kpi_9": True,
    }
    fail_kpi_9 = {
        "registration__management__fail_kpi_9": True,
    }

    pass_kpi_10 = {
        "pass_school_individual_healthcare_plan": True,
        "registration__management__pass_school_individual_healthcare_plan": True,
    }
    fail_kpi_10 = {
        "fail_school_individual_healthcare_plan": True,
        "registration__management__fail_school_individual_healthcare_plan": True,
    }

    case = e12_case_factory.create(
        organisations__organisation=ORGANISATION,
        # """age-dependent eligibility flag"""
        # **eligible_kpi_3_5_ineligible_6_8_10,
        **eligible_kpi_6_8_10_ineligible_3_5,
        # kpi 1
        **fail_kpi_1,
        # kpi 2
        **fail_kpi_2,
        # kpi 3 & 3b
        # **pass_kpi_3,
        # kpi 4
        **ineligible_kpi_4,
        # kpi 5
        # **pass_kpi_5,
        # kpi 6
        **fail_kpi_6,
        # kpi 7
        **ineligible_kpi_7,
        # kpi 8
        **fail_kpi_8,
        # kpi 9 (ALL)
        **fail_kpi_9,
        # kpi 10
        **fail_kpi_10,
    )

    registration = Registration.objects.get(case=case)

    calculate_kpis(registration)

    kpi = KPI.objects.get(pk=registration.pk)

    for attr, val in kpi.get_kpis().items():
        print(f"{attr}:{val}")
