from dataclasses import dataclass

@dataclass
class Product:
    code: int
    name: str
    maker: str
    price: float
    qty: int

    def total_cost(self) -> float:
        return self.price * self.qty

    def __str__(self):
        return f"{self.name} ({self.maker}) - {self.price} грн x {self.qty} = {self.total_cost()} грн"
