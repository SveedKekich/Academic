from dataclasses import dataclass, field
from datetime import date, datetime
from typing import List
import uuid


def generate_id() -> str:
    return str(uuid.uuid4())


@dataclass
class Room:
    id: str
    hotel_id: str
    number: str
    capacity: int
    price_per_day: float

    @staticmethod
    def from_dict(d: dict) -> "Room":
        return Room(
            id=d["id"],
            hotel_id=d["hotel_id"],
            number=d["number"],
            capacity=int(d["capacity"]),
            price_per_day=float(d["price_per_day"]),
        )


@dataclass
class Hotel:
    id: str
    name: str
    description: str
    rooms: List[Room] = field(default_factory=list)

    @staticmethod
    def from_dict(d: dict) -> "Hotel":
        rooms_data = d.get("rooms", [])
        rooms = [Room.from_dict(r) for r in rooms_data]
        return Hotel(
            id=d["id"],
            name=d["name"],
            description=d["description"],
            rooms=rooms
        )


@dataclass
class Client:
    id: str
    first_name: str
    last_name: str
    phone: str
    email: str

    @staticmethod
    def from_dict(d: dict) -> "Client":
        return Client(
            id=d["id"],
            first_name=d["first_name"],
            last_name=d["last_name"],
            phone=d["phone"],
            email=d["email"],
        )


@dataclass
class BookingRequest:
    id: str
    hotel_id: str
    room_id: str
    text: str
    start_date: date
    end_date: date

    @staticmethod
    def from_dict(d: dict) -> "BookingRequest":
        return BookingRequest(
            id=d["id"],
            hotel_id=d["hotel_id"],
            room_id=d["room_id"],
            text=d["text"],
            start_date=date.fromisoformat(d["start_date"]),
            end_date=date.fromisoformat(d["end_date"]),
        )


@dataclass
class Reservation:
    id: str
    hotel_id: str
    room_id: str
    client_id: str
    start_date: date
    end_date: date
    total_price: float
    is_cancelled: bool = False

    @staticmethod
    def from_dict(d: dict) -> "Reservation":
        return Reservation(
            id=d["id"],
            hotel_id=d["hotel_id"],
            room_id=d["room_id"],
            client_id=d["client_id"],
            start_date=date.fromisoformat(d["start_date"]),
            end_date=date.fromisoformat(d["end_date"]),
            total_price=float(d["total_price"]),
            is_cancelled=bool(d.get("is_cancelled", False)),
        )
