
from dataclasses import dataclass

@dataclass
class Product:
    code: str
    name: str
    manufacturer: str
    price: float
    quantity: int

    def total_value(self) -> float:
        """Total value of the batch (price * quantity)."""
        return self.price * self.quantity

    def increase_price(self, percent: float) -> None:
        """Increase price by a given percentage (e.g., 10 for +10%)."""
        if percent < -100:
            raise ValueError("Percent cannot reduce price below zero.")
        self.price *= (1 + percent / 100)

    def info(self) -> str:
        """Return formatted info about the product."""
        return (f"Code: {self.code}, Name: {self.name}, Manufacturer: {self.manufacturer}, "
                f"Price: {self.price:.2f}, Quantity: {self.quantity}, Total value: {self.total_value():.2f}")

    def __str__(self) -> str:
        return self.info()
