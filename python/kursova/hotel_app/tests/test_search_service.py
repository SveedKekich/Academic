import unittest

from hotel_app.bll.search_service import SearchService
from hotel_app.bll.models import Hotel, Client


class InMemoryRepo:
    def __init__(self):
        self.items = []

    def get_all(self):
        return list(self.items)

    def add(self, entity):
        self.items.append(entity)


class SearchServiceTests(unittest.TestCase):
    def setUp(self):
        self.hotel_repo = InMemoryRepo()
        self.client_repo = InMemoryRepo()

        h1 = Hotel(id="h1", name="Kyiv Plaza", description="Центральний готель", rooms=[])
        h2 = Hotel(id="h2", name="Sea View", description="Готель біля моря", rooms=[])
        self.hotel_repo.add(h1)
        self.hotel_repo.add(h2)

        c1 = Client(id="c1", first_name="Ivan", last_name="Ivanov", phone="123456", email="ivan@example.com")
        c2 = Client(id="c2", first_name="Petro", last_name="Petrenko", phone="987654", email="petro@sea.com")
        self.client_repo.add(c1)
        self.client_repo.add(c2)

        self.service = SearchService(self.hotel_repo, self.client_repo)

    def test_search_hotels_by_name(self):
        results = self.service.search_hotels("Kyiv")

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].id, "h1")

    def test_search_hotels_by_description(self):
        results = self.service.search_hotels("моря")

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].id, "h2")

    def test_search_clients_by_name(self):
        results = self.service.search_clients("Ivan")

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].id, "c1")

    def test_search_clients_by_email(self):
        results = self.service.search_clients("sea.com")

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].id, "c2")


if __name__ == "__main__":
    unittest.main()
