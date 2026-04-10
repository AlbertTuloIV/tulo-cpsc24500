

class MenuItem:
    def __init__(self, name: str, size: str, price: float):
        self.name = name
        self.size = size
        self.price = price

    def __str__(self) -> str:
        return f"{self.name} ({self.size}) - ${self.price:.2f}"