from cat import Cat
from dog import Dog
from fish import Fish

def adopt_pet(pets):
    print("\nWhat kind of pet would you like to adopt?")
    print("  1. Cat")
    print("  2. Dog")
    print("  3. Fish")
    choice = input("Choice: ").strip()

    name = input("Pet's name: ").strip()
    if not name:
        print("Name cannot be empty. Adoption canceled.")
        return
    
    if choice == "1":
        pets.append(Cat(name))
    elif choice == "2":
        breed = input("Breed: ").strip() or "Mixed"
        pets.append(Dog(name, breed))
    elif choice == "3":
        pets.append(Fish(name))
    else:
        print("Invalid choice. Adoption canceled.")
        return
    
    print(f"You adopted {pets[-1]}!")

def select_pet(pets):
    if not pets:
        print("You have no pets yet. Adopt one first.")
        return None
    
    print("\nYour pets:")
    for i, pet in enumerate(pets, start = 1):
        print(f"  {i}. {pet}")

    raw = input("Select a pet by number: ").strip()
    if not raw.isdigit():
        print("Invalid selection.")
        return None
    
    idx = int(raw) - 1
    if idx < 0 or idx >= len(pets):
        print("Out of range.")
        return None
    
    return pets[idx]

def view_all(pets):
    if not pets:
        print("No pets adopted yet.")
        return
    print("\n--- All Pets ---")
    for pet in pets:
        print(pet.status())

def print_menu():
    print("\n=== Pet Simulator ===")
    print("1. Adopt a pet")
    print("2. Feed a pet")
    print("3. Play with a pet")
    print("4. Put a pet to sleep")
    print("5. View all pets")
    print("6. Quit")

def main():
    pets = []

    while True:
        print_menu()
        choice = input("Choice: ").strip()

        if choice == "1":
            adopt_pet(pets)

        elif choice == "2":
            pet = select_pet(pets)
            if pet is not None:
                print(pet.feed())
                print(pet.status())
        
        elif choice == "3":
            pet = select_pet(pets)
            if pet is not None:
                print(pet.play())
                print(pet.status())
        
        elif choice == "4":
            pet = select_pet(pets)
            if pet is not None:
                print(pet.sleep())
                print(pet.status())
        
        elif choice == "5":
            view_all(pets)
        
        elif choice == "6":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice - pick 1-6.")

if __name__ == "__main__":
    main()