from circle import Circle
from gallery import Gallery
from rectangle import Rectangle
from triangle import Triangle

MENU = """\
======================================
Shape Gallery
======================================
(1) Add a circle
(2) Add a rectangle
(3) Add a triangle
(4) Display all shapes
(5) Show total area
(6) Show largest shape
(7) Quit
"""

def _prompt_float(prompt: str) -> float:
    return float(input(prompt).strip())

def _add_circle(gallery: Gallery) -> None:
    try:
        radius = _prompt_float("Enter radius: ")
        shape = Circle(radius)
        gallery.add_shape(shape)
        print(f"Added: {shape.describe()}")
    except ValueError as err:
        print(f"Could not add Circle: {err}")

def _add_rectagle(gallery: Gallery) -> None:
    try:
        width = _prompt_float("Enter width: ")
        height = _prompt_float("Enter height: ")
        shape = Rectangle(width, height)
        gallery.add_shape(shape)
        print(f"Added: {shape.describe()}")
    except ValueError as err:
        print(f"Could not add rectanble: {err}")

def _add_triangle(gallery: Gallery) -> None:
    try:
        a = _prompt_float("Enter side a: ")
        b = _prompt_float("Enter side b: ")
        c = _prompt_float("Enter side c: ")
        shape = Triangle(a, b, c)
        gallery.add_shape(shape)
        print(f"Added: {shape.describe()}")
    except ValueError as err:
        print(f"Could not add triangle: {err}")
    
def _show_total_area(gallery: Gallery) -> None:
    print(f"Total area: {gallery.total_area():.2f}")

def _show_largest_shape(gallery: Gallery) -> None:
    largest = gallery.largest_shape()
    if largest is None:
        print("Gallery is empty.")
    else:
        print(f"Largest shape: {largest.describe()} "
              f"(area: {largest.area():.2f})")

def main() -> None:
    gallery = Gallery("My Shapes")

    while True:
        print(MENU)
        try:
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                _add_circle(gallery)
            elif choice == "2":
                _add_rectagle(gallery)
            elif choice == "3":
                _add_triangle(gallery)
            elif choice == "4":
                gallery.display_all()
            elif choice == "5":
                _show_total_area(gallery)
            elif choice == "6":
                _show_largest_shape(gallery)
            elif choice == "7":
                print("Goodbye.")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 7.")
        
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye.")
            break
        except Exception as err:
            print(f"Unexpected error: {err}")

if __name__ == "__main__":
    main()