from .json_repository import JsonRepository
from ..bll.models import Hotel


class HotelRepository(JsonRepository[Hotel]):

    def __init__(self, filename: str = "data/hotels.json"):
        super().__init__(filename, Hotel)
