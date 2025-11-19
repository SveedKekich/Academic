import unittest
from datetime import date

from hotel_app.bll.booking_service import BookingService
from hotel_app.bll.models import Hotel, Room, Client, Reservation
from hotel_app.bll.exceptions import BookingError, ValidationError


class InMemoryRepo:
    
    def __init__(self):
        self.items = []

    def get_all(self):
        return list(self.items)

    def get_by_id(self, entity_id: str):
        for x in self.items:
            if x.id == entity_id:
                return x
        raise Exception(f"Not found: {entity_id}")

    def add(self, entity):
        self.items.append(entity)

    def update(self, entity):
        for i, x in enumerate(self.items):
            if x.id == entity.id:
                self.items[i] = entity
                return

    def delete(self, entity_id: str):
        self.items = [x for x in self.items if x.id != entity_id]


class BookingServiceTests(unittest.TestCase):
    def setUp(self):
        self.hotel_repo = InMemoryRepo()
        self.client_repo = InMemoryRepo()
        self.reservation_repo = InMemoryRepo()

        hotel = Hotel(
            id="h1",
            name="Test Hotel",
            description="Desc",
            rooms=[
                Room(id="r1", hotel_id="h1", number="101", capacity=2, price_per_day=100.0),
                Room(id="r2", hotel_id="h1", number="102", capacity=3, price_per_day=150.0),
            ],
        )
        client1 = Client(id="c1", first_name="Ivan", last_name="Ivanov", phone="123", email="a@b.com")
        client2 = Client(id="c2", first_name="Petro", last_name="Petrenko", phone="456", email="b@c.com")

        self.hotel_repo.add(hotel)
        self.client_repo.add(client1)
        self.client_repo.add(client2)

        self.service = BookingService(self.hotel_repo, self.client_repo, self.reservation_repo)

    def test_create_reservation_success(self):
        res = self.service.create_reservation(
            client_id="c1",
            hotel_id="h1",
            room_id="r1",
            start_date=date(2025, 1, 1),
            end_date=date(2025, 1, 4),
        )

        self.assertEqual(res.total_price, 3 * 100.0)
        self.assertEqual(len(self.reservation_repo.get_all()), 1)
        self.assertFalse(res.is_cancelled)

    def test_create_reservation_invalid_dates_raises(self):
        with self.assertRaises(ValidationError):
            self.service.create_reservation(
                client_id="c1",
                hotel_id="h1",
                room_id="r1",
                start_date=date(2025, 1, 10),
                end_date=date(2025, 1, 10),
            )

    def test_create_reservation_overlap_raises(self):
        existing = Reservation(
            id="res1",
            hotel_id="h1",
            room_id="r1",
            client_id="c1",
            start_date=date(2025, 1, 1),
            end_date=date(2025, 1, 5),
            total_price=400.0,
            is_cancelled=False,
        )
        self.reservation_repo.add(existing)

        with self.assertRaises(BookingError):
            self.service.create_reservation(
                client_id="c1",
                hotel_id="h1",
                room_id="r1",
                start_date=date(2025, 1, 3),
                end_date=date(2025, 1, 6),
            )

    def test_create_reservation_overlap_but_cancelled_ok(self):
        existing = Reservation(
            id="res1",
            hotel_id="h1",
            room_id="r1",
            client_id="c1",
            start_date=date(2025, 1, 1),
            end_date=date(2025, 1, 5),
            total_price=400.0,
            is_cancelled=True,
        )
        self.reservation_repo.add(existing)

        res = self.service.create_reservation(
            client_id="c1",
            hotel_id="h1",
            room_id="r1",
            start_date=date(2025, 1, 3),
            end_date=date(2025, 1, 6),
        )

        self.assertIsNotNone(res.id)
        self.assertEqual(len(self.reservation_repo.get_all()), 2)

    def test_cancel_reservation_sets_flag(self):
        res = Reservation(
            id="res1",
            hotel_id="h1",
            room_id="r1",
            client_id="c1",
            start_date=date(2025, 1, 1),
            end_date=date(2025, 1, 3),
            total_price=200.0,
            is_cancelled=False,
        )
        self.reservation_repo.add(res)

        self.service.cancel_reservation("res1")

        updated = self.reservation_repo.get_by_id("res1")
        self.assertTrue(updated.is_cancelled)

    def test_get_reservation_returns_correct(self):
        res = Reservation(
            id="res1",
            hotel_id="h1",
            room_id="r2",
            client_id="c2",
            start_date=date(2025, 2, 1),
            end_date=date(2025, 2, 5),
            total_price=600.0,
            is_cancelled=False,
        )
        self.reservation_repo.add(res)

        loaded = self.service.get_reservation("res1")

        self.assertEqual(loaded.id, "res1")
        self.assertEqual(loaded.room_id, "r2")
        self.assertEqual(loaded.client_id, "c2")

    def test_get_booked_rooms_on_date(self):
        res1 = Reservation(
            id="res1",
            hotel_id="h1",
            room_id="r1",
            client_id="c1",
            start_date=date(2025, 1, 1),
            end_date=date(2025, 1, 5),   # [1,5)
            total_price=400.0,
            is_cancelled=False,
        )
        res2 = Reservation(
            id="res2",
            hotel_id="h1",
            room_id="r2",
            client_id="c2",
            start_date=date(2025, 1, 3),
            end_date=date(2025, 1, 4),
            total_price=150.0,
            is_cancelled=False,
        )
        self.reservation_repo.add(res1)
        self.reservation_repo.add(res2)

        rooms = self.service.get_booked_rooms("h1", date(2025, 1, 3))

        numbers = sorted(r.number for r in rooms)
        self.assertEqual(numbers, ["101", "102"])

    def test_get_free_rooms_on_date(self):
        res1 = Reservation(
            id="res1",
            hotel_id="h1",
            room_id="r1",
            client_id="c1",
            start_date=date(2025, 1, 1),
            end_date=date(2025, 1, 5),
            total_price=400.0,
            is_cancelled=False,
        )
        self.reservation_repo.add(res1)

        free_rooms = self.service.get_free_rooms("h1", date(2025, 1, 2))

        self.assertEqual(len(free_rooms), 1)
        self.assertEqual(free_rooms[0].number, "102")

    def test_get_reservation_price(self):
        res = Reservation(
            id="res1",
            hotel_id="h1",
            room_id="r2",
            client_id="c1",
            start_date=date(2025, 3, 1),
            end_date=date(2025, 3, 4),
            total_price=3 * 150.0,
            is_cancelled=False,
        )
        self.reservation_repo.add(res)

        price = self.service.get_reservation_price("res1")

        self.assertEqual(price, 450.0)

    def test_get_reservation_price_details(self):
        res = Reservation(
            id="res1",
            hotel_id="h1",
            room_id="r1",
            client_id="c1",
            start_date=date(2025, 4, 1),
            end_date=date(2025, 4, 6),
            total_price=5 * 100.0,
            is_cancelled=False,
        )
        self.reservation_repo.add(res)

        days, price_per_day, total = self.service.get_reservation_price_details("res1")

        self.assertEqual(days, 5)
        self.assertEqual(price_per_day, 100.0)
        self.assertEqual(total, 500.0)

    def test_get_clients_with_reservations(self):
        self.reservation_repo.add(
            Reservation(
                id="res1",
                hotel_id="h1",
                room_id="r1",
                client_id="c1",
                start_date=date(2025, 5, 1),
                end_date=date(2025, 5, 3),
                total_price=200.0,
                is_cancelled=False,
            )
        )
        self.reservation_repo.add(
            Reservation(
                id="res2",
                hotel_id="h1",
                room_id="r2",
                client_id="c2",
                start_date=date(2025, 5, 2),
                end_date=date(2025, 5, 4),
                total_price=300.0,
                is_cancelled=False,
            )
        )

        clients = self.service.get_clients_with_reservations("h1")

        ids = sorted(c.id for c in clients)
        self.assertEqual(ids, ["c1", "c2"])


if __name__ == "__main__":
    unittest.main()
