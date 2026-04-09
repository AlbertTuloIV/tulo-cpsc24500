from menu_item import MenuItem
from order import Order

DRINKS = [
    ("Americano", 3.50),
    ("Cappucciono", 4.25),
    ("Espresso", 3.00),
    ("Latte", 4.75),
]

SIZES = [
    ("Small", 0.00),
    ("Medium", 0.75),
    ("Large", 1.25),
]

width = 44
title = "STARLIGHT COFFEE POS"

def main():
    print("*" * width)
    print(f"* {title.center(width - 4)} *")
    print("*" * width)

    name = input("What is your name? ")

    isOrdering = True
    order = Order(name)

    while isOrdering:
        print(f"What would you like? please enter 1-{DRINKS.count}")
        for i, (name, price) in enumerate(DRINKS, start=1):
            print(f"{i}. {name} - ${price:.2f}")
        
        goodInput = False
        while not goodInput:
            choice = input("Pick an Item: ")

            if choice.isdigit():
                choice = int(choice)

                if 1 <= choice <= len(DRINKS):
                    drink_name, base_price = DRINKS[choice - 1]
                    ## TODO: Add size functionality here
                    size_name = "Small"
                    size_upcharge = 0.00

                    line_price = base_price + size_upcharge

                    item = MenuItem(drink_name, size_name, line_price)

                    order.add_item(item)

                    print(f"Added: {item.name} for ${item.price:.2f}")

                    goodInput = True
                else:
                    print("Inavlid number. Try again.")
            else:
                    print("Please enter a valid number.")
        
        addMore = input("Would you like to add another item? y/n: ")
        if addMore == "n":
            isOrdering = False
            break
        else:
            continue


    print("you have completed ordering!")

        
        

    
        
        
    




if __name__ == "__main__":
    main()