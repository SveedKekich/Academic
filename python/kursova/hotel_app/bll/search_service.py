from typing import List
from .models import Hotel, Client


class SearchService:
    def __init__(self, hotel_repo, client_repo):
        self._hotel_repo = hotel_repo
        self._client_repo = client_repo

    def search_hotels(self, keyword: str) -> List[Hotel]:
        keyword = keyword.lower()
        result = []
        for h in self._hotel_repo.get_all():
            if keyword in h.name.lower() or keyword in h.description.lower():
                result.append(h)
        return result

    def search_clients(self, keyword: str) -> List[Client]:
        keyword = keyword.lower()
        result = []
        for c in self._client_repo.get_all():
            if (
                keyword in c.first_name.lower()
                or keyword in c.last_name.lower()
                or keyword in c.phone.lower()
                or keyword in c.email.lower()
            ):
                result.append(c)
        return result
