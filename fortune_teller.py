def main():
    # Welcome Message.
    print("*" * 60)
    print("*                   FORTUNE TELLER V1.0                    *")
    print("*" * 60)

    # Get users's name, age, favorite color.
    fullName = input("\nEnter your full name: ")
    age = int(input("Enter your age: "))
    favColor = input("Enter your favorite color: ")

    # Fortune teller calculations
    luckyNum = 8
    fortuneCategory = "Good Fortune"
    luckyPercentage = 75.000

    # Fortune teller reading
    print("\n")
    print("=" * 60)
    print("                    YOUR FORTUNE READING                     ")
    print("=" * 60)

    print("Name:              " + fullName)
    print("Name length:       " + str(len(fullName)))
    print("Age:               " + str(age))
    print("Favorite Color:    " + favColor)
    print("Lucky number:      " + str(luckyNum))
    print("Fortune category:  " + fortuneCategory)
    print("Lucky percentage:  " + f"{luckyPercentage:.3f}%")



if __name__ == "__main__":
    main()