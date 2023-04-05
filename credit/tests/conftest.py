import pytest

from factory import django, faker
from credit.models import LoanRequest

from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()


class LoanRequestFactory(django.DjangoModelFactory):
    class Meta:
        model = LoanRequest

    requested_amount = 3000
    personal_id = 12345678
    gender = "NA"
    first_name = faker.Faker("first_name")
    last_name = faker.Faker("last_name")
    email = faker.Faker("email")


@pytest.fixture(scope="session")
def create_loan_request():
    def _create_loan_request(**kwargs):

        loan_request = LoanRequestFactory.create(**kwargs)

        return loan_request

    return _create_loan_request


@pytest.fixture(scope="session")
def create_user():
    def _create_user(**kwargs):
        return User.objects.create(email="staff@mail.com", is_staff=True, password="something", **kwargs)

    return _create_user


@pytest.fixture(scope="session")
def create_authenticated_client():

    def _create_authenticated_client(user):
        client = APIClient()
        client.force_login(user)

        return client
    return _create_authenticated_client
