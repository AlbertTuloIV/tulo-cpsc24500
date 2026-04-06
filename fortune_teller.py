import random as rd

def main():
    # Declared to fill redundant code.
    ageError = "Invalid input. Please enter a positive number."

    fortuneList: list[tuple[str, str]] = [
        ("Adventure Awaits", "Your lucky number indicates that you will have an exciting adventure in the near future. Embrace new experiences and be open to change."),
        ("Caution Ahead", "Your lucky number suggests that you should be cautious in your upcoming endeavors. Take time to plan and consider your options."),
        ("Love is in the Air", "Your lucky number indicates that you may find love or strengthen existing relationships. Be open to new connections and cherish those around you."),
        ("Financial Stability", "Your lucky number suggests that you will experience financial stability. Focus on budgeting and saving to make the most of this fortunate period."),
        ("Career Success", "Your lucky number indicates that you will achieve success in your career. Stay focused and work hard to reach your goals."),
        ("Health and Wellness", "Your lucky number suggests that you should prioritize your health and wellness. Take care of yourself and make time for self-care."),
        ("Unexpected Blessings", "Your lucky number indicates that you will receive unexpected blessings. Stay positive and be open to the good things coming your way."),
        ("Personal Growth", "Your lucky number suggests that you will experience personal growth. Embrace challenges and learn from your experiences to become a better version of yourself."),
    ]

    # ANSI color codes for terminal text
    colorCodes = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "orange": "\033[38;5;208m",
        "purple": "\033[38;5;129m",
        "pink": "\033[38;5;213m",
    }
    resetCode = "\033[0m"
    

    # Welcome Message.
    print("*" * 60)
    print("*                   FORTUNE TELLER V1.0                    *")
    print("*" * 60)

    # Get user full name
    fullName = input("Enter your full name: ")    
    # Continues until a valid age is entered.
    goodAge = False
    while not goodAge:
        try:
            age = int(input("Enter your age: "))
            if not isValidAge(age):
                print(ageError)
            else:
                goodAge = True
        except ValueError:
            print(ageError)

    # Get user favorite color
    favColor = input("Enter your favorite color: ")
    colorCode = colorCodes.get(favColor.lower(), "")


    # Fortune teller calculations
    luckyNum = rd.randint(1, 10)
    luckyPercentage = luckyPercentageCalculator(age, luckyNum)
    fortune = fortuneTeller(luckyNum, luckyPercentage, fortuneList)
    fortuneCategory = fortune[0]
    fortuneMessage = fortune[1]
    
    # Fortune teller reading
    print("\n")
    try:
        with open("fortune_output.txt", "w") as f:
            def printAndWrite(text):
                print(text)
                f.write(text + "\n")

            printAndWrite("=" * 60)
            printAndWrite("                    YOUR FORTUNE READING                     ")
            printAndWrite("=" * 60)
            printAndWrite(f"Name:              {fullName.capitalize()}")
            printAndWrite(f"Name length:       {len(fullName)}")
            printAndWrite(f"Age:               {age}")
            printAndWrite(f"Favorite Color:    {favColor}")
            printAndWrite(f"Lucky number:      {luckyNum}")
            printAndWrite(f"Fortune category:  {fortuneCategory}")
            printAndWrite(f"Lucky percentage:  {luckyPercentage:.3f}%")
            if isValidColor(favColor):
                print(f"\nYour fortune:       \n{colorCode}{fortuneMessage}{resetCode}")
            else:
                print(f"\nYour fortune:       \n{fortuneMessage}")
            f.write(f"\nYour fortune:       \n{fortuneMessage}\n")
            printAndWrite("=" * 60)
    except IOError:
        print("An error occurred while writing to the file.")
        return
    
    print("\nFortune saved to fortune_output.txt")
    print("=" * 60)
    print(f"Goodbye, {fullName.split()[0].capitalize()}! May your fortune smile\nupon you!")
    print("=" * 60)

# This function determines the fortune category and message based on the user's lucky number and lucky percentage.
def fortuneTeller(luckyNum, luckyPercentage, fortuneList) -> tuple[str, str]:
    randFortune = rd.randint(1, 8)
    
    if luckyPercentage < 10:
        return fortuneList[randFortune - 1]
        
    else:
        if 0 < luckyNum <= 3:
            if luckyPercentage >= 50:
                return fortuneList[0]
            else:
                return fortuneList[1]
                        
        elif 3 < luckyNum <= 7:
            if luckyPercentage >= 50:
                return fortuneList[2]
            else:
                return fortuneList[3]
            
        elif 7 < luckyNum < 10:
            if luckyPercentage >= 50:
                return fortuneList[4]
            else:
                return fortuneList[5]

        elif luckyNum == 10:
            if luckyPercentage >= 50:
                return fortuneList[6]
            else:   
                return fortuneList[7]

# This function calculates the lucky percentage based on the user's age and lucky number.
def luckyPercentageCalculator(age, luckyNum):
   return (luckyNum / age * 100)

def isValidAge(age) -> bool:
    if age > 0:
        return True
    return False

# This function checks if the user's favorite color is valid and returns True or False accordingly.
def isValidColor(color) -> bool:
    validColors = ["red", "green", "yellow", "blue", "magenta", "cyan", "white", "orange", "purple", "pink"]
    if color.lower() in validColors:
        return True
    return False

if __name__ == "__main__":
    main()

