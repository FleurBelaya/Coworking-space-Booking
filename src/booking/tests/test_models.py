from datetime import date

import pytest

from booking.models import Reservation, Space, SpaceOwner


@pytest.mark.django_db
def test_space_owner_str():
    owner = SpaceOwner.objects.create(company_name="ООО Коворкинг")

    assert str(owner) == "ООО Коворкинг"


@pytest.mark.django_db
def test_space_str():
    owner = SpaceOwner.objects.create(company_name="ООО Коворкинг")

    space = Space.objects.create(
        space_name="Переговорная",
        space_description="Большая переговорная",
        price=1500,
        square=30,
        owner=owner,
    )

    assert str(space) == "Переговорная"


@pytest.mark.django_db
def test_reservation_str():
    owner = SpaceOwner.objects.create(company_name="ООО Коворкинг")

    space = Space.objects.create(
        space_name="Переговорная",
        space_description="Большая переговорная",
        price=1500,
        square=30,
        owner=owner,
    )

    reservation = Reservation.objects.create(
        start_time=date(2026, 7, 1),
        end_time=date(2026, 7, 5),
        space=space,
    )

    assert str(reservation) == "Переговорная (2026-07-01 - 2026-07-05)"
