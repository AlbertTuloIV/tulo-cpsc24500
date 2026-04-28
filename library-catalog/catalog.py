from library_item import LibraryItem

class Catalog:

    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._items = []
        return cls._instance
    
    def add_item(self, item: LibraryItem) -> None:
        if not isinstance(item, LibraryItem):
            raise TypeError("Only LibraryItem instances may be added.")
        self._items.append(item)
    
    def remove_item(self, title: str) -> int:
        key = title.lower()
        before = len(self._items)
        self._items = [i for i in self._items if i.title.lower() != key]
        return before - len(self._items)
    
    def search_by_title(self, keyword: str):
        k = keyword.lower()
        return [i for i in self._items if k in i.title.lower()]
    
    def search_by_author(self, keyword: str):
        k = keyword.lower()
        return [i for i in self._items if k in i.author.lower()]
    
    def get_all_items(self):
        return sorted(self._items)
    
    def get_checked_out_items(self):
        return sorted([i for i in self._items if i.checked_out])
    
    def get_available_items(self):
        return sorted([i for i in self._items if not i.checked_out])
    
    def find_by_exact_title(self, title: str):
        key = title.lower()
        for i in self._items:
            if i.title.lower() == key:
                return i
        return None
        
    def __len__(self):
        return len(self._items)