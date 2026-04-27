from collections import Counter

from word_collection import WordCollection
from story_template import TEMPLATES

def print_summary(words):
    print(f"Loaded {len(words)} words:")
    counts = Counter(w.part_of_speech for w in words)
    for pos in sorted(counts):
        print(f"  {pos}: {counts[pos]}")

def choose_template():
    print("\nAvailable story styles:")
    for i, t in enumerate(TEMPLATES, start = 1):
        print(f"   {i}. {t.name}")
    while True:
        choice = input("Choose a style: ").strip()
        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(TEMPLATES):
                return TEMPLATES[idx - 1]
        print("Invalid choice. Try again.")

def ask_count():
    while True:
        raw = input("How many sentences? ").strip()
        if raw.isdigit() and int(raw) > 0:
            return int(raw)
        print("Please enter a positive integer.")

def main():
    print("=" * 40)
    print("Welcome to StoryTeller")
    print("=" * 40)

    while True:
        path = input("Enter path to word file: ").strip()
        try:
            words = WordCollection.from_file(path)
            break
        except FileNotFoundError:
            print(f"File not found: {path}")
    
    print_summary(words)

    while True:
        template = choose_template()
        n = ask_count()
        print(f"\n--- {template.name} Story ---")
        for _ in range(n):
            print(template.generate(words))

        again = input("\nGenerate another story? (yes/no): ").strip().lower()
        if not again.startswith("y"):
            break

    print("Thank you for using StoryTeller!")

if __name__ == "__main__":
    main()