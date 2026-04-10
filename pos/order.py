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
            print(f"Removed {removed_item}")
        else:
            print("Invalid item number. Nothing removed.")
        
    def subtotal(self) -> float:
        return sum(item.price for item in self.items)
    
    def tax(self) -> float:
        return self.subtotal() * 0.0875 ## 8.75%
    
    def total(self) -> float:
        return self.subtotal() + self.tax()
    
    def __str__(self) -> str:
        lineItems = []
        lineItems.append(f"  Customer: {self.customer_name}")
        lineItems.append("-" * 44)

        if not self.items:
            lineItems.append("No items in order.")
        else:
            for i, item in enumerate(self.items, start=1):
                formattedName = f"{i}. {item.name} ({item.size})"
                formattedPrice = f"${item.price:.2f}"
                lineItems.append(f"  {formattedName:<30}{formattedPrice:>10}")

        
        subTotalText = "Subtotal:"
        taxText = "Tax (8.75%):"
        totalText = "TOTAL:"

        subtotalNumText = f"${self.subtotal():.2f}"
        taxNumText = f"${self.tax():.2f}"
        totalNumText = f"${self.total():.2f}"
        
        lineItems.append("-" * 44)
        lineItems.append(f"   {subTotalText:<30}{subtotalNumText:>10}")
        lineItems.append(f"   {taxText:<30}{taxNumText:>10}")
        lineItems.append("-" * 44)
        lineItems.append(f"   {totalText:<30}{totalNumText:>10}")

        return "\n".join(lineItems)