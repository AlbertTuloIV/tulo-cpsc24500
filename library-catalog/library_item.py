from abc import ABC, abstractmethod

class LibraryItem(ABC):

    def __init__(self, title: str, author: str, year: int, checked_out: bool = False):
        self._title = title
        self._author = author
        self._year = int(year)
        self._checked_out = bool(checked_out)

    @property
    def title(self) -> str:
        return self._title
    
    @title.setter
    def title(self, value: str) -> None:
        if not value or not str(value).strip():
            raise ValueError("Title cannot be empty.")
        self._title = str(value)

    @property
    def author(self) -> str:
        return self._author
    
    @author.setter
    def author(self, value: str) -> None:
        if not value or not str(value).strip():
            raise ValueError("Author cannot be empty.")
        self._author = str(value)
        
    @property
    def year(self) -> int:
        return self._year
    
    @year.setter
    def year(self, value: int) -> None:
        self._year = int(value)

    @property
    def checked_out(self) -> bool:
        return self._checked_out
    
    @abstractmethod
    def get_item_type(self) -> str:
        """RETURN A STRING IDENTIYING THE ITEM TYPE."""

    def check_out(self) -> None:
        if self._checked_out:
            raise RuntimeError(f"'{self._title}' is already checked out.")
        self._checked_out = True

    def check_in(self) -> None:
        if not self._checked_out:
            raise RuntimeError(f"'{self._title}' is not checked out.")
        self._checked_out = False

    def __lt__(self, other: "LibraryItem") -> bool:
        if not isinstance(other, LibraryItem):
            return NotImplemented
        return self._title_lower() < other._title.lower()
    
    def __str__(self) -> str:
        status = "CHECKED OUT" if self._checked_out else "AVAILABLE"
        return (f"[{self.get_item_type()}] {self._title} by {self._author} "
                f"({self._year}) - {status}")