from .json_repository import JsonRepository
from ..bll.models import Reservation


class ReservationRepository(JsonRepository[Reservation]):

    def __init__(self, filename: str = "data/reservations.json"):
        super().__init__(filename, Reservation)
