# Prompt the user to enter their name and store it in 'name'
name = input("Enter your name:\n")

# Print a welcome message with the user's name
print(f"Welcome {name}, to our store!")

# Prompt the user to enter their balance and store it as an integer in 'balance'
balance = int(input("Enter your balance: "))

# List of items with their prices per kg
items = {
    1: {"name": "Potato", "price": 50},
    2: {"name": "Apple", "price": 30}
}

# Print the list of items available for purchase
print("Here is the list of items:\n"
      "1: Potato 50/kg\n"
      "2: Apple 30/kg\n")

# Allow the user to select items
while True:
    try:
        # Prompt the user to enter their choice of item
        choice = int(input("Enter the number of the item you want to buy (or 0 to exit): "))
        
        # Exit the loop if the user enters 0
        if choice == 0:
            break
        
        # Check if the choice is valid
        if choice in items:
            item = items[choice]
            print(f"You selected {item['name']}. Price: {item['price']} per kg.")
            
            # Prompt the user to enter the quantity they want to buy
            quantity = float(input(f"Enter the quantity (in kg) you want to buy: "))
            cost = item['price'] * quantity
            
            # Check if the user has enough balance
            if cost <= balance:
                balance -= cost
                print(f"Purchase successful! You bought {quantity} kg of {item['name']}.")
                print(f"Remaining balance: {balance}")
            else:
                print("Insufficient balance. Please enter a lower quantity or add more funds.")
        else:
            print("Invalid item number. Please select a valid item.")
    
    except ValueError:
        print("Invalid input. Please enter a number.")

# Final message when the user exits the loop
print("Thank you for shopping with us!")