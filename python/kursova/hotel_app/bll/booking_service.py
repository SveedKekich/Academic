from datetime import date
from typing import List, Tuple

from .models import Reservation, Hotel, Client, Room, generate_id
from .exceptions import BookingError, ValidationError


class BookingService:
    def __init__(self, hotel_repo, client_repo, reservation_repo):
        self._hotel_repo = hotel_repo
        self._client_repo = client_repo
        self._reservation_repo = reservation_repo


    def _get_hotel_and_room(self, hotel_id: str, room_id: str) -> Tuple[Hotel, Room]:
        hotel = self._hotel_repo.get_by_id(hotel_id)
        room = next((r for r in hotel.rooms if r.id == room_id), None)
        if room is None:
            raise BookingError("Номер не знайдено в даному готелі")
        return hotel, room

    def _dates_overlap(self, s1: date, e1: date, s2: date, e2: date) -> bool:
        return not (e1 <= s2 or e2 <= s1)

    def create_reservation(
        self,
        client_id: str,
        hotel_id: str,
        room_id: str,
        start_date: date,
        end_date: date,
    ) -> Reservation:
        if end_date <= start_date:
            raise ValidationError("Дата виїзду має бути пізніше дати заїзду")

        client: Client = self._client_repo.get_by_id(client_id)
        hotel, room = self._get_hotel_and_room(hotel_id, room_id)

        for res in self._reservation_repo.get_all():
            if res.hotel_id == hotel_id and res.room_id == room_id and not res.is_cancelled:
                if self._dates_overlap(res.start_date, res.end_date, start_date, end_date):
                    raise BookingError("Номер вже заброньований на цей період")

        days = (end_date - start_date).days
        total_price = days * room.price_per_day

        reservation = Reservation(
            id=generate_id(),
            hotel_id=hotel_id,
            room_id=room_id,
            client_id=client.id,
            start_date=start_date,
            end_date=end_date,
            total_price=total_price,
        )
        self._reservation_repo.add(reservation)
        return reservation

    def cancel_reservation(self, reservation_id: str) -> None:
        res = self._reservation_repo.get_by_id(reservation_id)
        res.is_cancelled = True
        self._reservation_repo.update(res)

    def get_reservation(self, reservation_id: str) -> Reservation:
        return self._reservation_repo.get_by_id(reservation_id)

    def get_booked_rooms(self, hotel_id: str, on_date: date) -> List[Room]:
        hotel = self._hotel_repo.get_by_id(hotel_id)
        booked_room_ids = set()
        for res in self._reservation_repo.get_all():
            if res.hotel_id == hotel_id and not res.is_cancelled:
                if res.start_date <= on_date < res.end_date:
                    booked_room_ids.add(res.room_id)
        return [r for r in hotel.rooms if r.id in booked_room_ids]

    def get_free_rooms(self, hotel_id: str, on_date: date) -> List[Room]:
        hotel = self._hotel_repo.get_by_id(hotel_id)
        booked = set(r.id for r in self.get_booked_rooms(hotel_id, on_date))
        return [r for r in hotel.rooms if r.id not in booked]

    def get_reservation_price(self, reservation_id: str) -> float:
        res = self._reservation_repo.get_by_id(reservation_id)
        return res.total_price

    def get_clients_with_reservations(self, hotel_id: str) -> List[Client]:
        client_ids = {
            res.client_id
            for res in self._reservation_repo.get_all()
            if res.hotel_id == hotel_id and not res.is_cancelled
        }
        result = []
        for cid in client_ids:
            result.append(self._client_repo.get_by_id(cid))
        return result
    def get_reservation_price_details(self, reservation_id: str) -> tuple[int, float, float]:
        res = self._reservation_repo.get_by_id(reservation_id)
        _, room = self._get_hotel_and_room(res.hotel_id, res.room_id)

        days = (res.end_date - res.start_date).days
        if days <= 0:
            raise ValidationError("Невірний період бронювання")

        price_per_day = room.price_per_day
        total_price = res.total_price  

        return days, price_per_day, total_price