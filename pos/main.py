from menu_item import MenuItem
from order import Order

DRINKS = [
    ("Americano", 3.50),
    ("Cappuccino", 4.25),
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
invalidChoiceMsg = "Please enter a valid number."

def main():
    print("*" * width)
    print(f"* {title.center(width - 4)} *")
    print("*" * width)

    customerName = input("What is your name? ")

    isOrdering = True
    order = Order(customerName)
    orderStep = 1

    while isOrdering:

        match orderStep:
            ### Main Menu Options ###
            case 0:
                goodOption = False
                print("What would you like to do?")
                print("  1. Add another drink")
                print("  2. Remove a drink")
                print("  3. View order")
                print("  4. Check out")
                print("  5. Leave")
                while not goodOption:
                    try:
                        userChoice = int(input("Choice: \n"))
                        if not checkInput(userChoice, 5):
                            print(invalidChoiceMsg)
                        else:
                            goodOption = True
                            orderStep = userChoice
                    except ValueError:
                        print(invalidChoiceMsg)

            ### Drink Ordering ###
            case 1:
                print(f"--- Drink Menu ---")
                for i, (name, price) in enumerate(DRINKS, start=1):
                    drinkPriceFormat = f"${price:.2f}"
                    print(f"   {i}. {name:<15}{drinkPriceFormat:>5}")

                cancel_option = len(DRINKS) + 1
                print(f"   {cancel_option}. Cancel")
                
                
                while True:
                    try:
                        drinkChoice = int(input(f"Choose a drink: (1-{len(DRINKS) + 1}): "))
                    except ValueError:
                        print(invalidChoiceMsg)
                        continue

                    if drinkChoice == cancel_option:
                        print("Going back...")
                        if int(len(order.items)) < 1:
                            orderStep = 5
                            break
                        else:
                            orderStep = 0
                            break
                    
                    elif 1 <= drinkChoice <= len(DRINKS):
                        drink_name, base_price = DRINKS[drinkChoice - 1]

                        print("\n--- Size ---")
                        for i, (name, price) in enumerate(SIZES, start=1):
                            sizePriceFormat = f"+${price:.2f}"

                            print(f"   {i}. {name:<10}{sizePriceFormat:>5}")

                        #### Size Logic ###
                        while True:
                            try:
                                sizeChoice = int(input(f"Choose a size: (1-{len(SIZES)}): "))
                            except ValueError:
                                print(invalidChoiceMsg)
                                continue
                                                                
                            if 1 <= sizeChoice <= len(SIZES):
                                size_name, size_upcharge = SIZES[sizeChoice - 1]
                                line_price = base_price + size_upcharge
                                item = MenuItem(drink_name, size_name, line_price)  
                                order.add_item(item)

                                print(f"Added: {item.name} ({item.size}) - ${item.price:.2f}\n")
                                
                                orderStep = 0
                                break
                            else:
                                print(invalidChoiceMsg)
                        break
            
            ### Order Item Removal ###
            case 2:
                if int(len(order.items)) < 1:
                    print("There are no drinks to remove. Please add a drink to your order.")
                    orderStep = 1
                else:
                    print("\n Which item would you like to remove from your order?")
                    for i, item in enumerate(order.items, start=1):
                        print(f"   {i}. {item.name} ({item.size}) - ${item.price:.2f}")
                    
                    goodChoice = False
                    while not goodChoice:
                        choice = int(input(f"Please select item: (1-{len(order.items)}): "))

                        if not checkInput(choice, len(order.items)):
                            print(invalidChoiceMsg)
                        else:
                            order.remove_item(choice)
                            if int(len(order.items)) < 1:
                                orderStep = 1    
                                goodChoice = True
                            else:
                                orderStep = 0
                                goodChoice = True
            
            ### Order Summary ###
            case 3:
                orderViewText = "Current Order Details"
                print("=" * width)
                print(f"{title.center(width)}")
                print(f"{orderViewText.center(width)}")
                print("=" * width)
                print(order.__str__())
                orderStep = 0
            
            ### Check out ###
            case 4:
                receiptText = "RECEIPT"
                farewellMessage = f"Thank you, {customerName}! Enjoy your coffee."
                receiptTitle = "STARLIGHT COFFEE"
                print("=" * width)
                print(f"{receiptTitle.center(width)}")
                print(f"{receiptText.center(width)}")
                print("=" * width)
                print(order.__str__())
                print("=" * width)
                print(f"{farewellMessage.center(width)}")
                print("=" * width)
                isOrdering = False
            
            ### Cancel / Leave ###
            case 5:
                if len(order.items) > 0:
                    print("You still have items in your order!\n")
                
                while True:                        
                    willLeave = input("Are you sure you want to leave? y/n: ")
                    try:
                        if yesNoCheck(willLeave):
                            if willLeave.lower() == "y":
                                print("Thank you for stopping by!")
                                isOrdering = False
                                break
                            else:
                                orderStep = 0
                                break
                        else:
                            print("Please only type 'y' or 'n'")
                            willLeave = ""
                    except ValueError:
                        print("Please only type 'y' or 'n'")
                        willLeave = ""
        
def checkInput(choice, maxChoice) -> bool:
    if 0 < choice <= maxChoice:
        return True
    return False

def yesNoCheck(charYN) -> bool:
    if charYN.lower() not in ["n", "y"] or len(charYN) != 1:
        return False
    return True
    

if __name__ == "__main__":
    main()