import random

def choose_level():
    print("\nChoose difficulty level:")
    print("1) Easy   (1–20, 8 tries)")
    print("2) Medium (1–50, 7 tries)")
    print("3) Hard   (1–100, 6 tries)")
    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        return (1, 20, 8)
    elif choice == "2":
        return (1, 50, 7)
    elif choice == "3":
        return (1, 100, 6)
    else:
        print("Invalid choice, defaulting to Easy.")
        return (1, 20, 8)

def play_game():
    low, high, max_tries = choose_level()
    number = random.randint(low, high)
    attempts = 0
    print(f"\nI'm thinking of a number between {low} and {high}. You have {max_tries} tries.")

    while attempts < max_tries:
        raw = input(f"Attempt {attempts+1}/{max_tries}: ")
        if not raw.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(raw)
        if not low <= guess <= high:
            print(f"Your guess must be between {low} and {high}.")
            continue

        attempts += 1

        if guess == number:
            print(f"🎉 Correct! You found it in {attempts} attempts.")
            return
        elif guess < number:
            print("↑ Too low! Try a higher number.")
        else:
            print("↓ Too high! Try a lower number.")

    print(f"😢 Out of tries! The number was {number}.")

if __name__ == "__main__":
    play_game()

