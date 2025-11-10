from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, first_name: str, last_name: str, gender: str, address: str = ""):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.address = address

    @abstractmethod
    def info(self) -> str:
        pass
