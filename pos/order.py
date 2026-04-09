from menu_item import MenuItem

class Order:
    def __init__(self, customer_name: str):
        self.customer_name = customer_name
        self.items: list[MenuItem] = []
    
    def add_item(self, item: MenuItem) -> None:
        self.items.append(item)

    def remove_item(self, index: int) -> None:
        actual_index = index - 1

        if 0 <= actual_index < len(self.items):
            removed_item = self.items.pop(actual_index)
            print(f"Removed {removed_item.name}")
        else:
            print("Invalid item number. Nothing removed.")
        
    def subtotal(self) -> float:
        return sum(item.price for item in self.items)
        
    def tax(self) -> float:
        return self.subtotal() * 0.0875 ## 8.75%
        
    def __str__(self) -> str:
        lineItems = []
        lineItems.append(f"Customer: {self.customer_name}")
        lineItems.append("-" * 30)

        if not self.items:
            lineItems.append("No items in order.")
        else:
            for i, item in enumerate(self.items, start=1):
                lineItems.append(f"{i}. {item}")
        
        lineItems.append("-" * 30)
        lineItems.append(f"Subtotal: ${self.subtotal():.2f}")
        lineItems.append(f"Tax (8.75%): ${self.tax():.2f}")
        lineItems.append(f"Total: ${self.total():.2f}")

        return "\n".join(lineItems)