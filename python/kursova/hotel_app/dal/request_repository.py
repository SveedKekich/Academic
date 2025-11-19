from .json_repository import JsonRepository
from ..bll.models import BookingRequest


class BookingRequestRepository(JsonRepository[BookingRequest]):

    def __init__(self, filename: str = "data/requests.json"):
        super().__init__(filename, BookingRequest)
