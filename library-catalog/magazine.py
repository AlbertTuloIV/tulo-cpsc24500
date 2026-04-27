from library_item import LibraryItem

class Magazine(LibraryItem):
    def __init__(self, title, author, year, issue_number: int, month: str, checked_out: bool = False):
        super().__init__(title, author, year, checked_out)
        self._issue_number = int(issue_number)
        self._month = str(month)

    @property
    def issue_number(self) -> int:
        return self._issue_number
    
    @property
    def month(self) -> str:
        return self._month
    
    def get_item_type(self) -> str:
        return "Magazine"
    
    def __str__(self) -> str:
        return (f"{super().__str__()} | Issue: {self._issue_number}, "
                f"Month: {self._month}")