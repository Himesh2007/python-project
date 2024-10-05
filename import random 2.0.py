import random  # Import the random module to generate random numbers

# Function to play the number guessing game
def guess_number():
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
    
    # Welcome message and instructions for the game
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Can you guess it?")
    
    # Initialize the number of attempts
    attempts = 0
    
    # Start an infinite loop to keep asking for guesses until the correct one is found
    while True:
        # Get the user's guess and convert it to an integer
        guess = int(input("Enter your guess: "))
        attempts += 1  # Increment the number of attempts

        # Provide feedback based on the guess
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            # If the guess is correct, congratulate the user and display the number of attempts
            print(f"Congratulations! You guessed the number {number} correctly!")
            print(f"It took you {attempts} attempts.")
            
            # Generate a random gift amount between 100 and 10,000
            gift = random.randint(100, 10000)
            print(f"You won Rs{gift}")
            break  # Exit the loop when the correct guess is made

# Call the guess_number function if the script is run directly
if __name__ == "__main__":
    guess_number()