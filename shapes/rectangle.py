from shape import Shape

class Rectangle(Shape):

    def __init__(self, width: float, height: float) -> None:
        if not isinstance(width, (int, float)) or width <= 0:
            raise ValueError("Width must be a positive number.")
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Height must be a positive number.")
        self.widht = float(width)
        self.height = float(height)

    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)
    
    def describe(self) -> str:
        return f"Rectable {self.width} x {self.height}"