from datetime import timedelta

import pytest
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APIClient

from booking.models import Reservation, Space, SpaceOwner


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def owner():
    return SpaceOwner.objects.create(company_name="ООО Коворкинг")


@pytest.fixture
def space(owner):
    return Space.objects.create(
        space_name="Переговорная",
        space_description="Большая переговорная",
        price=1500,
        square=30,
        owner=owner,
    )


@pytest.mark.django_db
def test_get_spaces(api_client, space):
    response = api_client.get("/spaces/")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1


@pytest.mark.django_db
def test_create_space(api_client, owner):
    response = api_client.post(
        "/spaces/create/",
        {
            "space_name": "Конференц-зал",
            "space_description": "Для мероприятий",
            "price": "5000.00",
            "square": 100,
            "owner": owner.id,
        },
        format="json",
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert Space.objects.count() == 1


@pytest.mark.django_db
def test_delete_space(api_client, space):
    response = api_client.delete(f"/spaces/{space.id}/delete/")

    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_get_owner_spaces(api_client, owner, space):
    response = api_client.get(f"/owners/{owner.id}/spaces/")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1


@pytest.mark.django_db
def test_create_reservation(api_client, space):
    today = timezone.localdate()

    response = api_client.post(
        "/reservations/create/",
        {
            "start_time": today,
            "end_time": today + timedelta(days=2),
            "space": space.id,
        },
        format="json",
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert Reservation.objects.count() == 1


@pytest.mark.django_db
def test_delete_reservation(api_client, space):
    today = timezone.localdate()

    reservation = Reservation.objects.create(
        start_time=today,
        end_time=today + timedelta(days=2),
        space=space,
    )

    response = api_client.delete(f"/reservations/{reservation.id}/delete/")

    assert response.status_code == status.HTTP_204_NO_CONTENT
