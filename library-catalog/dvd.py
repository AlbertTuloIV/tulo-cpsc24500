from library_item import LibraryItem

class DVD(LibraryItem):
    def __init__(self, title, author, year, runtime_minutes: int, rating: str, checked_out: bool = False):
        super().__init__(title, author, year, checked_out)
        self._runtime_minutes = int(runtime_minutes)
        self._rating = str(rating)

    @property
    def runtime_minutes(self) -> int:
        return self._runtime_minutes
    
    @property
    def rating(self) -> str:
        return self._rating
    
    def get_item_type(self) -> str:
        return "DVD"
    
    def __str__(self) -> str:
        return (f"{super().__str__()} | Runtime: {self._runtime_minutes} min, "
                f"Rating: {self._rating}")