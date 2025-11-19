from typing import List
from .models import Client, generate_id
from .exceptions import ValidationError


class ClientService:
    def __init__(self, repo):
        self._repo = repo


    def create_client(self, first_name: str, last_name: str, phone: str, email: str) -> Client:
        if not first_name or not last_name:
            raise ValidationError("Ім'я та прізвище не можуть бути порожніми")
        client = Client(
            id=generate_id(),
            first_name=first_name.strip(),
            last_name=last_name.strip(),
            phone=phone.strip(),
            email=email.strip(),
        )
        self._repo.add(client)
        return client

    def delete_client(self, client_id: str) -> None:
        self._repo.delete(client_id)

    def update_client(self, client: Client) -> None:
        if not client.first_name or not client.last_name:
            raise ValidationError("Ім'я та прізвище не можуть бути порожніми")
        self._repo.update(client)

    def get_client(self, client_id: str) -> Client:
        return self._repo.get_by_id(client_id)

    def get_all_clients(self) -> List[Client]:
        return self._repo.get_all()

    def sort_by_first_name(self) -> List[Client]:
        return sorted(self._repo.get_all(), key=lambda c: c.first_name.lower())

    def sort_by_last_name(self) -> List[Client]:
        return sorted(self._repo.get_all(), key=lambda c: c.last_name.lower())
