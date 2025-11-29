import random

def start_playing():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 20. Can you guess it ?")
    number = random.randint(1, 20)
    attempts = 0

    while True:
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

        if not 1 <= guess <= 20:
            print("Your guess must be between 1 and 20.")
            continue

        elif guess < number:
            print("Too low! Try a higher number.")
            attempts += 1
            print(f"Attempts left: {8 - attempts}")
        elif guess > number:
            print("Too high! Try a lower number.")
            attempts += 1
            print(f"Attempts left: {8 - attempts}")
        
        else:
            print(f"🎉 Correct! You found it in {attempts} attempts.")
            i = input("Would you like to play again? (y)(n): ").strip().lower()
            if i == 'y':
                start_playing()                                                    # Methodu tekrar cagirip donguye tekrar basliyoruz.
            else:
                print("Thanks for playing! Goodbye!")
                break
            

start_playing()             #Fonksyionu\Methodu cagiriyoruz.



# tekrar oynamak ister misin  ve cikis icin (y) eklenmeli 