from datetime import timedelta

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from booking.models import Reservation, Space, SpaceOwner


class Command(BaseCommand):
    help = "Fill database with test data"

    @transaction.atomic
    def handle(self, *args, **options):
        Reservation.objects.all().delete()
        Space.objects.all().delete()
        SpaceOwner.objects.all().delete()

        owners = [
            SpaceOwner.objects.create(company_name="Группа Творческих Пространств"),
            SpaceOwner.objects.create(company_name="Бизнес Площадки"),
            SpaceOwner.objects.create(company_name="Арт Сообщество"),
        ]

        space_1 = Space.objects.create(
            space_name="Фотостудия Свет",
            space_description="Профессиональная фотостудия для съёмок",
            price=120.00,
            square=80,
            owner=owners[0],
        )

        space_2 = Space.objects.create(
            space_name="Фотостудия Рассвет",
            space_description="Студия с большим количеством естественного света",
            price=150.00,
            square=95,
            owner=owners[1],
        )

        space_3 = Space.objects.create(
            space_name="Творческий Лофт",
            space_description="Пространство для мероприятий и фотосессий",
            price=200.00,
            square=150,
            owner=owners[2],
        )

        space_4 = Space.objects.create(
            space_name="Арт-Пространство",
            space_description="Уютное пространство для творчества",
            price=90.00,
            square=60,
            owner=owners[0],
        )

        space_5 = Space.objects.create(
            space_name="Бизнес-Зал",
            space_description="Помещение для встреч и конференций",
            price=300.00,
            square=200,
            owner=owners[1],
        )

        today = timezone.localdate()

        Reservation.objects.create(
            start_time=today + timedelta(days=1),
            end_time=today + timedelta(days=3),
            space=space_1,
        )

        Reservation.objects.create(
            start_time=today + timedelta(days=3),
            end_time=today + timedelta(days=5),
            space=space_1,
        )

        Reservation.objects.create(
            start_time=today + timedelta(days=6),
            end_time=today + timedelta(days=8),
            space=space_2,
        )

        Reservation.objects.create(
            start_time=today + timedelta(days=8),
            end_time=today + timedelta(days=10),
            space=space_3,
        )

        Reservation.objects.create(
            start_time=today + timedelta(days=10),
            end_time=today + timedelta(days=12),
            space=space_4,
        )

        Reservation.objects.create(
            start_time=today + timedelta(days=12),
            end_time=today + timedelta(days=15),
            space=space_5,
        )

        self.stdout.write(self.style.SUCCESS("Тестовые данные успешно загружены в БД"))
