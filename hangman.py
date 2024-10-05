import random  # Import the random module for selecting random words

def choose_word():
    # List of possible words for the game
    words = ["python", "programming", "hangman", "game", "challenge"]
    # Randomly choose and return a word from the list
    return random.choice(words)

def play_hangman():
    # Choose a word for the player to guess
    word = choose_word()
    
    # Set to keep track of guessed letters
    guessed_letters = set()
    
    # Number of attempts allowed
    attempts = 6
    
    # Welcome message
    print("Welcome to Hangman!")
    
    # Game loop that continues until attempts run out
    while attempts > 0:
        # Create a string that shows the current state of the word
        display_word = "".join([letter if letter in guessed_letters else "_" for letter in word])
        
        # Print the current state of the word
        print(f"Word: {display_word}")
        
        # Prompt the user to guess a letter
        guess = input("Guess a letter: ").lower()
        
        # Validate the user's input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            # Add the guessed letter to the set of guessed letters
            guessed_letters.add(guess)
            # Check if all letters in the word have been guessed
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            # Decrease the number of attempts left
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")
    
    # If attempts run out, reveal the word
    if attempts == 0:
        print(f"Game over! The word was: {word}")

# Start the hangman game
play_hangman()