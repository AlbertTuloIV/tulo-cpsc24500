import math

from shape import Shape

class Circle(Shape):

    def __init__(self, radius: float) -> None:
        if not isinstance(radius, (int, float)) or radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = float(radius)

    def area(self) -> float:
        return math.pi * self.radius ** 2
    
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius
    
    def describe(self) -> str:
        return f"Circle with radius {self.radius}"