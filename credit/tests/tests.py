import pytest

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from credit.models import LoanRequest


@pytest.mark.django_db
def test_create_loan_request():

    url = reverse("credit-list")

    data = {
        "personal_id": "1234567",
        "first_name": "Cacho",
        "last_name": "Fontana",
        "gender": "male",
        "email": "cacho.fontana@mail.com",
        "requested_amount": 1200
    }

    client = APIClient()

    response = client.post(url, data, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert LoanRequest.objects.first().first_name == "Cacho"

# DETAIL not True

# create
@pytest.mark.django_db
def test_create_loan_request_fail():

    url = reverse("credit-list")

    # Falta personal_id como campo
    data = {
        "first_name": "Cacho",
        "last_name": "Fontana",
        "gender": "male",
        "email": "cacho.fontana@mail.com",
        "requested_amount": 1200
    }

    client = APIClient()

    response = client.post(url, data, format="json")

    assert response.status_code == status.HTTP_400_BAD_REQUEST


# list
@pytest.mark.django_db
def test_loan_request_list(create_loan_request, create_user, create_authenticated_client):

    loan_request = create_loan_request()

    url = reverse("credit-list")
    client = create_authenticated_client(create_user())

    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.data, list)
    assert response.data[0]["first_name"] == loan_request.first_name


# Retrieve
@pytest.mark.django_db
def test_loan_request_retrieved_by_id(create_loan_request, create_user, create_authenticated_client):

    loan_request = create_loan_request()

    url = reverse("credit-detail", kwargs={"pk": loan_request.id})
    client = create_authenticated_client(create_user())

    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["first_name"] == loan_request.first_name


# Update
@pytest.mark.django_db
def test_loan_request_retrieved_by_id(create_loan_request, create_user, create_authenticated_client):

    loan_request = create_loan_request()

    url = reverse("credit-detail", kwargs={"pk": loan_request.id})
    client = create_authenticated_client(create_user())

    data = {
        "approved": True
    }

    response = client.patch(url, data, format="json")

    loan_request.refresh_from_db()
    assert response.status_code == status.HTTP_200_OK
    assert loan_request.approved is True


# Delete
@pytest.mark.django_db
def test_loan_request_is_deleted(create_loan_request, create_user, create_authenticated_client):

    loan_request = create_loan_request()

    url = reverse("credit-detail", kwargs={"pk": loan_request.id})
    client = create_authenticated_client(create_user())
    response = client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert LoanRequest.objects.first() is None
