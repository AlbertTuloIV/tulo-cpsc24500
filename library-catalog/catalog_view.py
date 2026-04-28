class CatalogView:

    MENU = (
        "\n=============================\n"
        "    Library Catalog System\n"
        "=============================\n"
        "1. List all items\n"
        "2. Search by title\n"
        "3. Search by author\n"
        "4. Check out item\n"
        "5. Check in item\n"
        "6. Add new item\n"
        "7. View checked-out items\n"
        "8. Save and quit"
    )

    def display_menu(self) -> None:
        print(self.MENU)
    
    def display_message(self, message: str) -> None:
        print(message)
    
    def display_items(self, items, header: str = "--- All Items (sorted by title) ---"):
        print(header)
        if not items:
            print("(no items)")
            return
        for item in items:
            print(item)
    
    def display_search_results(self, items, query: str) -> None:
        header = f'--- Search Results for "{query} ---'
        if not items:
            print(header)
            print("(no matches)")
            return
        self.display_items(items, header)