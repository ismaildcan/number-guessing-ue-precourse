import random
from pathlib import Path

SCORES_FILE = Path("scores.txt")

def choose_level():
    print("\nChoose difficulty level:")
    print("1) Easy   (1–20, 8 tries)")
    print("2) Medium (1–50, 7 tries)")
    print("3) Hard   (1–100, 6 tries)")
    choice = input("Enter 1, 2, or 3: ").strip()
    if choice == "1":
        return ("Easy", 1, 20, 8)
    elif choice == "2":
        return ("Medium", 1, 50, 7)
    elif choice == "3":
        return ("Hard", 1, 100, 6)
    else:
        print("Invalid choice, defaulting to Easy.")
        return ("Easy", 1, 20, 8)

def save_score(name: str, level_name: str, result: str, attempts: int):
    # result: "win" or "lose"
    with open(SCORES_FILE, "a", encoding="utf-8") as f:
        f.write(f"{name},{level_name},{result},{attempts}\n")

def show_scores():
    if not SCORES_FILE.exists():
        print("\nNo scores yet.")
        return
    print("\n— Scores —")
    with open(SCORES_FILE, "r", encoding="utf-8") as f:
        for line in f:
            name, level, result, attempts = line.strip().split(",")
            print(f"{name:12s} | {level:6s} | {result:4s} | {attempts} attempts")

def play_round(name: str):
    level_name, low, high, max_tries = choose_level()
    number = random.randint(low, high)
    attempts = 0
    print(f"\nI'm thinking of a number between {low} and {high}. You have {max_tries} tries.")

    while attempts < max_tries:
        raw = input(f"Attempt {attempts+1}/{max_tries}: ").strip()
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
            save_score(name, level_name, "win", attempts)
            return
        print("↑ Too low! Try higher." if guess < number else "↓ Too high! Try lower.")

    print(f"😢 Out of tries! The number was {number}.")
    save_score(name, level_name, "lose", attempts)

def main():
    print("🎲 Number Guessing — Score Edition")
    name = input("Enter your name (for the score board): ").strip() or "Player"

    while True:
        # play one round
        play_round(name)

        # post-round menu loop (accept p/s/e/x)
        while True:
            opt = input("\n[p]lay again, [s]how scores, or [e]xit: ").lower().strip()
            if opt in ("p", ""):
                # play again -> break inner loop, go to next round
                break
            elif opt in ("s", "score", "scores"):
                show_scores()
            elif opt in ("e", "x", "q", "exit"):
                print("Bye!")
                return
            else:
                print("Invalid option. Type p, s, or e.")
