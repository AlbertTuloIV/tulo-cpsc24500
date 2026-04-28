import os
import sys

from catalog import Catalog
from catalog_view import CatalogView
from item_factory import ItemFactory

DATA_FILE = os.path.join("data", "catalog.tsv")

def load_catalog(catalog: Catalog, path: str) -> int:
    if not os.path.exists(path):
        print(f"Warning: data file '{path}' not found. Starting empty.")
        return 0
    count = 0
    with open(path, "r", encoding="utf-8") as f:
        for lineno, raw in enumerate(f, start = 1):
            line = raw.rstrip("\n").rstrip("\r")
            if not line.strip():
                continue
            parts = line.split("\t")
            if len(parts) < 7:
                print(f"Skipping malformed line {lineno}: {line!r}")
                continue
            item_type, title, author, year, e1, e2, checked = parts[:7]
            try:
                item = ItemFactory.create_item(
                    item_type, title, author, year, e1, e2, checked
                )
                catalog.add_item(item)
                count += 1
            except (ValueError, TypeError) as e:
                print(f"Skipping line {lineno}: {e}")
    
    return count

def save_catalog(catalog: Catalog, path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for item in catalog.get_all_items():
            t = item.get_item_type()
            if t == "Book":
                e1, e2 = item.isbn, item.page_count
            elif t == "DVD":
                e1, e2 = item.runtime_minutes, item.rating
            else:
                e1, e2 = item.issue_number, item.month
            checked = "true" if item.checked_out else "false"
            f.write("\t".join(str(x) for x in [
                t, item.title, item.author, item.year, e1, e2, checked
            ]) + "\n")

def prompt(text: str) -> str:
    try:
        return input(text)
    except EOFError:
        return ""
    
def add_item_flow(catalog: Catalog, view: CatalogView) -> None:
    item_type = prompt("Item type (Book/DVD/Magazine): ").strip()
    title = prompt("Title: ").strip()
    author = prompt("Author: ").strip()
    year = prompt("Year: ").strip()
    try:
        if item_type.lower() == "book":
            isbn = prompt("ISBN: ").strip()
            pages = prompt("Page count: ").strip()
            item = ItemFactory.create_item(item_type, title, author, year, isbn, pages)
        elif item_type.lower() == "dvd":
            runtime = prompt("Runtime (minutes): ").strip()
            rating = prompt("Rating: ").strip()
            item = ItemFactory.create_item(item_type, title, author, year, runtime, rating)
        elif item_type.lower() == "magazine":
            issue = prompt("Issue Number: ").strip()
            month = prompt("Month: ").strip()
            item = ItemFactory.create_item(item_type, title, author, year, issue, month)
        else:
            view.display_message(f"Unkown item type: {item_type}")
            return
        catalog.add_item(item)
        view.display_message(f"Added: {item.title}")
    except ValueError as e:
        view.display_message(f"Could not add item: {e}")

def main() -> int:
    catalog = Catalog()
    view = CatalogView()

    try:
        loaded = load_catalog(catalog, DATA_FILE)
        view.display_message(f"Catalog loaded: {loaded} items.")
    except OSError as e:
        view.display_message(f"error reading catalog file: {e}")

    while True:
        view.display_menu()
        choice = prompt("Enter choice: ").strip()

        if choice == "1":
            view.display_items(catalog.get_all_items())
        elif choice == "2":
            q = prompt("Enter title to search: ").strip()
            view.display_search_results(catalog.search_by_title(q), q)
        elif choice == "3":
            q = prompt("Enter author to search: ").strip()
            view.display_search_results(catalog.search_by_author(q), q)
        elif choice == "4":
            t = prompt("Enter the exact title to check out: ").strip()
            item = catalog.find_by_exact_title(t)
            if item is None:
                view.display_message(f"No item found with title '{t}'.")
            else:
                try:
                    item.check_out()
                    view.display_message(f"Successfully checked out : {item.title}")
                except RuntimeError as e:
                    view.display_message(str(e))
        elif choice == "5":
            t = prompt("Enter the exact title to check in: ").strip()
            item = catalog.find_by_exact_title(t)
            if item is None:
                view.display_message(f"No item found with title '{t}'.")
            else:
                try:
                    item.check_in()
                    view.display_message(f"Successfully checked in: {item.title}")
                except RuntimeError as e:
                    view.display_message(str(e))
        elif choice == "6":
            add_item_flow(catalog, view)
        elif choice == "7":
            view.display_items(catalog.get_checked_out_items(), header="--- Checked-Out Items ---")
        elif choice == "8":
            try:
                save_catalog(catalog, DATA_FILE)
                view.display_message("Catalog saved. Goodbye!")
            except OSError as e:
                view.display_message(f"Error saving catalog: {e}")
            return 0
        else:
            view.display_message("Invalid choice. Please enter 1-8.")

if __name__ == "__main__":
    sys.exit(main())