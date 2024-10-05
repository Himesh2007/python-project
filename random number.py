import random  # Import the random module to generate random numbers

# Define a function for the number guessing game
def guess_number():
    number = random.randint(1, 100)  # Generate a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")  # Print a welcome message
    print("I have chosen a number between 1 and 100. Can you guess it?")  # Inform the user about the game
    attempts = 0  # Initialize the attempt counter

    while True:  # Loop until the correct number is guessed
        guess = int(input("Enter your guess: "))  # Prompt the user to enter their guess and convert it to an integer
        attempts += 1  # Increment the number of attempts

        if guess < number:  # Check if the guess is lower than the chosen number
            print("Too low! Try again.")  # Inform the user that their guess is too low
        elif guess > number:  # Check if the guess is higher than the chosen number
            print("Too high! Try again.")  # Inform the user that their guess is too high
        else:
            print(f"Congratulations! You guessed the number {number} correctly!")  # Congratulate the user for guessing correctly
            print(f"It took you {attempts} attempts.")  # Print the number of attempts made
            break  # Exit the loop after a correct guess

# Check if the script is run directly
if __name__ == "__main__":
    guess_number()  # Call the guess_number function to start the game