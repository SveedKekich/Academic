import unittest

from hotel_app.bll.client_service import ClientService
from hotel_app.bll.models import Client
from hotel_app.bll.exceptions import ValidationError


class InMemoryRepo:
    def __init__(self):
        self.items = []

    def get_all(self):
        return list(self.items)

    def get_by_id(self, entity_id: str):
        for x in self.items:
            if x.id == entity_id:
                return x
        raise Exception("Not found")

    def add(self, entity):
        self.items.append(entity)

    def update(self, entity):
        for i, x in enumerate(self.items):
            if x.id == entity.id:
                self.items[i] = entity
                return

    def delete(self, entity_id: str):
        self.items = [x for x in self.items if x.id != entity_id]


class ClientServiceTests(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryRepo()
        self.service = ClientService(self.repo)

    def test_create_client_success(self):
        c = self.service.create_client("Ivan", "Ivanov", "123", "a@b.com")
        
        self.assertIsNotNone(c.id)
        self.assertEqual(len(self.repo.get_all()), 1)
        self.assertEqual(c.first_name, "Ivan")

    def test_create_client_empty_name_raises(self):
        with self.assertRaises(ValidationError):
            self.service.create_client("", "Ivanov", "123", "a@b.com")

    def test_delete_client_removes_it(self):
        c = self.service.create_client("Ivan", "Ivanov", "123", "a@b.com")
        self.service.delete_client(c.id)
        self.assertEqual(len(self.repo.get_all()), 0)

    def test_update_client_changes_data(self):
        c = self.service.create_client("Ivan", "Ivanov", "123", "a@b.com")
        c.first_name = "Petro"
        c.last_name = "Petrenko"

        self.service.update_client(c)

        updated = self.repo.get_by_id(c.id)
        self.assertEqual(updated.first_name, "Petro")
        self.assertEqual(updated.last_name, "Petrenko")

    def test_get_client_returns_correct(self):
        c = self.service.create_client("Ivan", "Ivanov", "123", "a@b.com")
        loaded = self.service.get_client(c.id)
        self.assertEqual(loaded.id, c.id)

    def test_sort_by_first_name(self):
        self.service.create_client("Petro", "Bbbb", "1", "1@a.com")
        self.service.create_client("Andrii", "Aaaa", "2", "2@a.com")

        sorted_clients = self.service.sort_by_first_name()

        self.assertEqual([c.first_name for c in sorted_clients], ["Andrii", "Petro"])

    def test_sort_by_last_name(self):
        self.service.create_client("Ivan", "Zzz", "1", "1@a.com")
        self.service.create_client("Petro", "Aaa", "2", "2@a.com")

        sorted_clients = self.service.sort_by_last_name()

        self.assertEqual([c.last_name for c in sorted_clients], ["Aaa", "Zzz"])


if __name__ == "__main__":
    unittest.main()
