import datetime as dt

def main():
    print("Welcome Python!\n")
    name = input("What is your name?")
    print("=" * 60)
    print(f"Welcome {name} to CPSC24500!")
    print(f"\nToday is {dt.datetime.now().strftime('%Y-%m-%d')}")
    print("=" * 60)


if __name__ == "__main__":
    main()