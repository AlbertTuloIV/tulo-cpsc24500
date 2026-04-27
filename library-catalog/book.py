from library_item import LibraryItem

class Book(LibraryItem):
    def __init__(self, title, author, year, isbn: str, page_count: int, checked_out: bool = False):
        super().__init__(title, author, year, checked_out)
        self._isbn = str(isbn)
        self._page_count = int(page_count)

    @property
    def isbn(self) -> str:
        return self._isbn
    
    @property
    def page_count(self) -> int:
        return self._page_count
    
    def get_item_type(self) -> str:
        return "Book"
    
    def __str__(self) -> str:
        return (f"{super().__str__()} | ISBN: {self._isbn}, "
                f"Pages: {self._page_count}")