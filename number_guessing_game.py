import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 200.")
    print("You have 10 attempts to guess it correctly.")

    # Generate a random number between 1 and 200
    secret_number = random.randint(1, 200)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            guess = int(input("\nEnter your guess (1-200): "))
            if guess < 1 or guess > 200:
                print("Please enter a number within the valid range (1-200).")
                continue
            
            attempts += 1

            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts.")
                break

            if attempts == max_attempts:
                print("\nGame Over! You have used all your attempts.")
                print(f"The correct number was {secret_number}.")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == "yes" or play_again == "y":
        number_guessing_game()
    else:
        print("Thank you for playing the Number Guessing Game!")

if __name__ == "__main__":
    number_guessing_game()
