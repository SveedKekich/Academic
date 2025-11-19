from datetime import date
from typing import List

from .models import Hotel, Room, BookingRequest, generate_id
from .exceptions import ValidationError


class HotelService:
    def __init__(self, hotel_repo, request_repo):
        self._hotel_repo = hotel_repo
        self._request_repo = request_repo


    def add_hotel(self, name: str, description: str) -> Hotel:
        if not name:
            raise ValidationError("Назва готелю не може бути порожньою")
        hotel = Hotel(id=generate_id(), name=name.strip(), description=description.strip())
        self._hotel_repo.add(hotel)
        return hotel

    def delete_hotel(self, hotel_id: str) -> None:
        self._hotel_repo.delete(hotel_id)

    def get_hotel(self, hotel_id: str) -> Hotel:
        return self._hotel_repo.get_by_id(hotel_id)

    def get_all_hotels(self) -> List[Hotel]:
        return self._hotel_repo.get_all()

    def add_room(self, hotel_id: str, number: str, capacity: int, price_per_day: float) -> Room:
        hotel = self._hotel_repo.get_by_id(hotel_id)
        room = Room(
            id=generate_id(),
            hotel_id=hotel_id,
            number=number,
            capacity=capacity,
            price_per_day=price_per_day,
        )
        hotel.rooms.append(room)
        self._hotel_repo.update(hotel)
        return room

    def add_request(self, hotel_id: str, room_id: str, text: str,
                    start_date: date, end_date: date) -> BookingRequest:
        if end_date <= start_date:
            raise ValidationError("Дата виїзду має бути пізніше дати заїзду")
        req = BookingRequest(
            id=generate_id(),
            hotel_id=hotel_id,
            room_id=room_id,
            text=text.strip(),
            start_date=start_date,
            end_date=end_date,
        )
        self._request_repo.add(req)
        return req

    def delete_request(self, request_id: str) -> None:
        self._request_repo.delete(request_id)

    def update_request_text(self, request_id: str, new_text: str) -> BookingRequest:
        req = self._request_repo.get_by_id(request_id)
        req.text = new_text.strip()
        self._request_repo.update(req)
        return req

    def get_requests_in_period(self, hotel_id: str, from_date: date, to_date: date) -> List[BookingRequest]:
        result = []
        for req in self._request_repo.get_all():
            if req.hotel_id != hotel_id:
                continue
            if req.end_date >= from_date and req.start_date <= to_date:
                result.append(req)
        return result
