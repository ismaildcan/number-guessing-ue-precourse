import random

def main():
    print("🎲 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 20.")
    number = random.randint(1, 20)
    attempts = 0

    while True:
        raw = input("Enter your guess (1–20): ")

        if not raw.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(raw)

        if not 1 <= guess <= 20:
            print("Your guess must be between 1 and 20.")
            continue

        attempts += 1

        if guess < number:
            print("↑ Too low! Try a higher number.")
        elif guess > number:
            print("↓ Too high! Try a lower number.")
        else:
            print(f"🎉 Correct! You found it in {attempts} attempts.")
            break

if __name__ == "__main__":
    main()

