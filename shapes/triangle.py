import math

from shape import Shape

class Triangle(Shape):

    def __init__(self, side_a: float, side_b: float, side_c: float) -> None:
        for label, value in (("side_a", side_a),
                            ("side_b", side_b),
                            ("side_C", side_c)):
            if not isinstance(value, (int, float)) or value <= 0:
                raise ValueError(f"{label} must be a positive number.")
            
        a, b, c = float(side_a), float(side_b), float(side_c)

        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            raise ValueError(
                "Invalid triangle: the sum of any two sides "
                "must be greater than the third side."
            )
        
        self.side_a = a
        self.side_b = b
        self.side_c = c

    def area(self) -> float:
        a, b, c = self.side_a, self.side_b, self.side_c
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    def perimeter(self) -> float:
        return self.side_a + self.side_b + self.side_c
    
    def describe(self) -> str:
        return(
            f"Tirangle with sides "
            f"{self.side_a}, {self.side_b}, {self.side_c}"
        )