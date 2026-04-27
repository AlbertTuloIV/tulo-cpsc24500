from shape import Shape

class Gallery:

    def __init__(self, name: str) -> None:
        self.name = name
        self._shapes: list[Shape] = []

    def add_shape(self, shape: Shape) -> None:
        if not isinstance(shape, Shape):
            raise TypeError("Only Shape instances can be added to the gallery.")
        self._shapes.append(shape)

    def total_area(self) -> float:
        if not self._shapes:
            return 0.0
        return sum(s.area() for s in self._shapes)
    
    def largest_shape(self) -> Shape | None:
        if not self._shapes:
            return None
        return max(self._shapes, key=lambda s: s.area())
    
    def display_all(self) -> None:
        count = len(self._shapes)
        print(f"Gallery: {self.name} ({count} shapes)")
        print("-" * 60)
        for index, shape in enumerate(self._shapes, start = 1):
            print(f"{index}. {shape.describe()}")
            print(f"    Area: {shape.area():.2f}    "
                f"Perimeter: {shape.perimeter():.2f}")
        print("-" * 60)