import random
prize = ("Jacket" , "Car" , "Laptop" , "Mobile")
def guess_number():
    secret_number = random.randint(1, 100)    
    attempts = 0
    print("Welcome to the Guessing Game!")
    print("I've picked a number between 1 and 100. Try to guess it!")
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number}!")
                print(f"You made {attempts} attempts.")
                l = random.choice(prize)
                print(f"And your prize is {l}!")
                break
        except ValueError:
            print("Please enter a valid number.")
if __name__ == "__main__":
    guess_number()