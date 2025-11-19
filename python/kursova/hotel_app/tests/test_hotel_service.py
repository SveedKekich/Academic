import unittest
from datetime import date

from hotel_app.bll.hotel_service import HotelService
from hotel_app.bll.models import Hotel, Room, BookingRequest
from hotel_app.bll.exceptions import ValidationError


class InMemoryRepo:
    def __init__(self):
        self.items = []

    def get_all(self):
        return list(self.items)

    def get_by_id(self, entity_id: str):
        for x in self.items:
            if x.id == entity_id:
                return x
        raise Exception("Not found")

    def add(self, entity):
        self.items.append(entity)

    def update(self, entity):
        for i, x in enumerate(self.items):
            if x.id == entity.id:
                self.items[i] = entity
                return

    def delete(self, entity_id: str):
        self.items = [x for x in self.items if x.id != entity_id]


class HotelServiceTests(unittest.TestCase):
    def setUp(self):
        self.hotel_repo = InMemoryRepo()
        self.request_repo = InMemoryRepo()
        self.service = HotelService(self.hotel_repo, self.request_repo)

    def test_add_hotel_success(self):
        h = self.service.add_hotel("Test Hotel", "Nice")

        self.assertIsNotNone(h.id)
        self.assertEqual(len(self.hotel_repo.get_all()), 1)

    def test_add_hotel_empty_name_raises(self):
        with self.assertRaises(ValidationError):
            self.service.add_hotel("", "Desc")

    def test_add_room_to_hotel(self):
        h = self.service.add_hotel("Test Hotel", "Desc")

        room = self.service.add_room(h.id, "101", 2, 100.0)

        loaded = self.hotel_repo.get_by_id(h.id)
        self.assertEqual(len(loaded.rooms), 1)
        self.assertEqual(loaded.rooms[0].number, "101")
        self.assertEqual(room.id, loaded.rooms[0].id)

    def test_add_request_success(self):
        h = self.service.add_hotel("Test Hotel", "Desc")
        room = self.service.add_room(h.id, "101", 2, 100.0)

        req = self.service.add_request(
            hotel_id=h.id,
            room_id=room.id,
            text="Прошу забронювати",
            start_date=date(2025, 1, 1),
            end_date=date(2025, 1, 5),
        )

        self.assertIsNotNone(req.id)
        self.assertEqual(len(self.request_repo.get_all()), 1)

    def test_add_request_invalid_dates_raises(self):
        h = self.service.add_hotel("Test Hotel", "Desc")
        room = self.service.add_room(h.id, "101", 2, 100.0)

        with self.assertRaises(ValidationError):
            self.service.add_request(
                hotel_id=h.id,
                room_id=room.id,
                text="Bad dates",
                start_date=date(2025, 1, 5),
                end_date=date(2025, 1, 5),
            )

    def test_update_request_text(self):
        h = self.service.add_hotel("Test Hotel", "Desc")
        room = self.service.add_room(h.id, "101", 2, 100.0)
        req = self.service.add_request(
            hotel_id=h.id,
            room_id=room.id,
            text="Old text",
            start_date=date(2025, 1, 1),
            end_date=date(2025, 1, 3),
        )

        updated = self.service.update_request_text(req.id, "New text")

        self.assertEqual(updated.text, "New text")

    def test_get_requests_in_period(self):
        h = self.service.add_hotel("Test Hotel", "Desc")
        room = self.service.add_room(h.id, "101", 2, 100.0)

        r1 = self.service.add_request(
            hotel_id=h.id,
            room_id=room.id,
            text="Req1",
            start_date=date(2025, 1, 1),
            end_date=date(2025, 1, 5),
        )
        r2 = self.service.add_request(
            hotel_id=h.id,
            room_id=room.id,
            text="Req2",
            start_date=date(2025, 2, 1),
            end_date=date(2025, 2, 3),
        )

        requests = self.service.get_requests_in_period(
            h.id,
            from_date=date(2025, 1, 3),
            to_date=date(2025, 1, 10),
        )

        self.assertEqual(len(requests), 1)
        self.assertEqual(requests[0].id, r1.id)


if __name__ == "__main__":
    unittest.main()
