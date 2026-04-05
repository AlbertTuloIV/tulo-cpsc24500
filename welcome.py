import datetime as dt
import random as rd

def main():
    print("Welcome Python!\n")
    name = input("What is your name?")
    print("=" * 60)
    print(f"Welcome {name} to CPSC24500!")
    print(f"\nToday is {dt.datetime.now().strftime('%Y-%m-%d')}")
    print("=" * 60)
    funFact = "Python was named after the British comedy group Monty Python, not the snake!"
    randomNum = rd.randint(1, 50)
    print(f"\nFun Fact: {funFact}")
    guess = int(input(f"\nGuess a number between 1 and 50:"))
    correctGuess = False
    if guess == randomNum:
        correctGuess = True
    
    if correctGuess:
        print(f"Congratulations! You guessed the correct number!\nThe correct number was {randomNum}.")
    else:
        print(f"Sorry, that's not correct. The correct number was {randomNum}.")

    numberX = 1.5
    numberY = 2.5
    print(f"\nNumber X is 1.5")
    print(f"Number Y is 2.5")
    print(f"\nThat means X + Y is {numberX + numberY}")

if __name__ == "__main__":
    main()