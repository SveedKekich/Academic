from .json_repository import JsonRepository
from ..bll.models import Client


class ClientRepository(JsonRepository[Client]):

    def __init__(self, filename: str = "data/clients.json"):
        super().__init__(filename, Client)
