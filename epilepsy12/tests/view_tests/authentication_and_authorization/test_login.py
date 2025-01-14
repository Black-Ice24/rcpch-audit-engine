"""
- [ ] user can login with correct credentials
- [ ] user cannot login with wrong credentials
- [ ] user can login if password within 90 days of last update
- [ ] user cannot login if password not within 90 days of last update

- [ ] can create user with correct credentials
- [ ] cannot create user with wrong credentials
"""

# python imports
import pytest

# 3rd party imports
from django.urls import reverse

# E12 imports
from epilepsy12.forms import Epilepsy12UserUpdatePasswordForm
from epilepsy12.models import Epilepsy12User
from epilepsy12.tests.UserDataClasses import (
    test_user_rcpch_audit_team_data,
)


@pytest.mark.django_db
def test_pass_validation(
    client,
    seed_groups_fixture,
    seed_users_fixture,
):
    """
    Testing password reset/creation validation.

    All password validation happens in the form.

    REQUIREMENTS
        Minimum of 10 characters (minimum 16 for RCPCH Audit team)
        Must contain ONE capital
        Must contain ONE number
        Must contain ONE symbol from !@£$%^&*()_-+=|~
        Must NOT be exclusively numbers
        Must NOT be same as your email, name, surname
    """

    rcpch_user = Epilepsy12User.objects.get(
        first_name=test_user_rcpch_audit_team_data.role_str
    )

    # VALID PASSWORD
    PASSWORD = "Ep!lepsy12_Audit"

    form = Epilepsy12UserUpdatePasswordForm(
        user=rcpch_user,
        data={
            "new_password1": PASSWORD,
            "new_password2": PASSWORD,
        },
    )

    assert form.is_valid()

    INCORRECT_USER_PASSWORD_TOO_SHORT = (
        "Ep!lepsy12"  # 10 digits, 1 capital letter, one digit, one symbol
    )
    INCORRECT_USER_PASSWORD_TOO_SHORT = "Ep!lepsy"
    INCORRECT_USER_PASSWORD_NO_CAPITAL = "ep!lepsy12"
    INCORRECT_USER_PASSWORD_NO_SYMBOL = "Epilepsy12"
    INCORRECT_USER_PASSWORD_NO_NUMBER = "EpilepsyTwelve"
    INCORRECT_USER_PASSWORD_ALL_NUMBERS = "1234567890"
    INCORRECT_USER_PASSWORD_PREDICTABLE = "password"

    incorrect_passwords = [
        INCORRECT_USER_PASSWORD_TOO_SHORT,
        INCORRECT_USER_PASSWORD_TOO_SHORT,
        INCORRECT_USER_PASSWORD_NO_CAPITAL,
        INCORRECT_USER_PASSWORD_NO_SYMBOL,
        INCORRECT_USER_PASSWORD_NO_NUMBER,
        INCORRECT_USER_PASSWORD_ALL_NUMBERS,
        INCORRECT_USER_PASSWORD_PREDICTABLE,
    ]

    for incorrect_password in incorrect_passwords:
        form = Epilepsy12UserUpdatePasswordForm(
            user=rcpch_user,
            data={
                "new_password1": incorrect_password,
                "new_password2": incorrect_password,
            },
        )

    assert form.is_valid() is False


@pytest.mark.django_db
def test_unsuccessful_login_lockout(client):
    """Testing auto-lockout after 5 unsuccessful login attempts."""

    rcpch_user = Epilepsy12User.objects.get(
        first_name=test_user_rcpch_audit_team_data.role_str
    )
    
    # 5 failed login attempts
    
    for _ in range(5):
    
        login_response = client.post(
            reverse('login'),
            data={
                'rcpch_login_view-current_step' : 'auth',
                'auth-username': rcpch_user.email,
                'auth-password' : 'incorrect password',
                'auth-captacha_1': 'PASSED',
            }
        )     
    
    # After 5 failed logins, attempt one more
    login_response = client.post(
            reverse('login'),
            data={
                'rcpch_login_view-current_step' : 'auth',
                'auth-username': rcpch_user.email,
                'auth-password' : 'pw',
                'auth-captacha_1': 'PASSED',
            }
        )   
    
    # this is the item including errors
    assert login_response.context[12]['errors'][0] == "You have failed to login 5 or more consecutive times. You have been locked out for 10 minutes"

    