import random

<<<<<<< HEAD
def start_playing():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 20. Can you guess it ?")
=======
def main():
    print("🎲 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 20.")
>>>>>>> 744695cbbf01a7b6b74fd1b5dc34a5b6cd8797b2
    number = random.randint(1, 20)
    attempts = 0

    while True:
<<<<<<< HEAD
        if attempts == 10:
            print(f"Out of attempts! The number was {number}.")
            break

        raw_guess = input("\nPress (x) to exit...\nEnter your guess: ").lower()
        
        
        if raw_guess == "x":
            print("Exiting the game... Goodbye loser!")
            break

        if not raw_guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        guess = int(raw_guess)
=======
        raw = input("Enter your guess (1–20): ")

        if not raw.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(raw)
>>>>>>> 744695cbbf01a7b6b74fd1b5dc34a5b6cd8797b2

        if not 1 <= guess <= 20:
            print("Your guess must be between 1 and 20.")
            continue

<<<<<<< HEAD
        elif guess < number:
            print("Too low! Try a higher number.")
            attempts += 1
            print(f"Attempts left: {8 - attempts}")
        elif guess > number:
            print("Too high! Try a lower number.")
            attempts += 1
            print(f"Attempts left: {8 - attempts}")
        
        else:
            print(f"Correct! You found it in {attempts} attempts.")
            i = input("Would you like to play again? (y)(n): ").strip().lower()
            if i == 'y':
                start_playing()                                                    # Methodu tekrar cagirip donguye tekrar basliyoruz.
            else:
                print("Thanks for playing! Goodbye!")
                break
            

start_playing()             #Fonksyionu\Methodu cagiriyoruz.



# tekrar oynamak ister misin  ve cikis icin (y) eklenmeli 
=======
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

>>>>>>> 744695cbbf01a7b6b74fd1b5dc34a5b6cd8797b2
