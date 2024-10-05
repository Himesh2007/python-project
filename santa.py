import random  # Import the random module to generate random numbers

# Tuple containing the available prizes
prize = ("Jacket", "Car", "Laptop", "Mobile")

# Function to handle the number guessing game
def guess_number():
    secret_number = random.randint(1, 100)  # Generate a random number between 1 and 100
    attempts = 0  # Initialize the number of attempts
    print("Welcome to the Guessing Game!")  # Print a welcome message
    print("I've picked a number between 1 and 100. Try to guess it!")  # Inform the user about the game
    
    while True:  # Loop until the correct number is guessed
        try:
            guess = int(input("Enter your guess: "))  # Prompt user to enter their guess and convert it to an integer
            attempts += 1  # Increment the number of attempts
            if guess < secret_number:  # Check if the guess is lower than the secret number
                print("Too low! Try again.")  # Inform the user that their guess was too low
            elif guess > secret_number:  # Check if the guess is higher than the secret number
                print("Too high! Try again.")  # Inform the user that their guess was too high
            else:
                print(f"Congratulations! You've guessed the number {secret_number}!")  # Congratulate the user for guessing correctly
                print(f"You made {attempts} attempts.")  # Print the number of attempts made
                l = random.choice(prize)  # Randomly select a prize from the tuple
                print(f"And your prize is {l}!")  # Print the prize
                break  # Exit the loop after a correct guess
        except ValueError:  # Handle the case where the input is not a valid integer
            print("Please enter a valid number.")  # Inform the user to enter a valid number

# Check if the script is executed directly
if __name__ == "__main__":
    guess_number()  # Call the guess_number function to start the game