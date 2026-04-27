from book import Book
from dvd import DVD
from magazine import Magazine

class ItemFactory:

    @classmethod
    def create_item(cls, item_type: str, title: str, author: str, year, *extras):
        t = item_type.strip().lower()
        if t == "book":
            if len(extras) < 2:
                raise ValueError("Book requires isbn and page_count.")
            isbn, page_count, *rest = extras
            checked_out = cls._coerce_bool(rest[0]) if rest else False
            return Book(title, author, int(year), isbn, int(page_count), checked_out)
        
        if t == "dvd":
            if len(extras) < 2:
                raise ValueError("DVD requires runtime_minutes and rating.")
            runtime, rating, *rest = extras
            checked_out = cls._coerce_bool(rest[0]) if rest else False
            return DVD(title, author, int(year), int(runtime), rating, checked_out)
        
        if t == "magazine":
            if len(extras) < 2:
                raise ValueError("Magazine requires issue_number and month.")
            issue, month, *rest = extras
            checked_out = cls._coerce_bool(rest[0]) if rest else False
            return Magazine(title, author, int(year), int(issue), month, checked_out)

        raise ValueError(f"Unkown item type: {item_type}")
    
    @staticmethod
    def _coerce_bool(value) -> bool:
        if isinstance(value, bool):
            return value
        return str(value).strip().lower() == "true"