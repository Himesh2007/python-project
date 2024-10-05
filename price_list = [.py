class Item:
    # Initialize an Item object with name, price, and weight
    def __init__(self, name, price, weight):
        self.name = name  # Set the name of the item
        self.price = price  # Set the price of the item
        self.weight = weight  # Set the weight of the item

    # Define the string representation of the Item object
    def __str__(self):
        return f"{self.name} - Price: ${self.price}, Weight: {self.weight} kg"

    # Update the weight of the item and adjust the price accordingly
    def update_weight(self, new_weight):
        if new_weight < self.weight:  # Check if the new weight is less than the current weight
            self.price *= (new_weight / self.weight)  # Adjust price based on the weight reduction
            self.weight = new_weight  # Update the weight
        else:  # If new weight is more than or equal to the current weight
            self.price = self.price * (new_weight / self.weight)  # Adjust price based on the weight increase
            self.weight = new_weight  # Update the weight

class Cart:
    # Initialize a Cart object with an empty list of items
    def __init__(self):
        self.items = []  # Create an empty list to hold items in the cart

    # Add an item to the cart
    def add_item(self, item):
        self.items.append(item)  # Append the item to the list of items in the cart

    # Calculate the total price of all items in the cart
    def total_price(self):
        return sum(item.price for item in self.items)  # Sum the price of each item in the cart

# Function to display items with their index
def display_items(items):
    for i, item in enumerate(items):  # Enumerate over the list of items with index
        print(f"{i+1}. {item}")  # Print the index and the item

def main():
    # Create a list of Item objects
    items = [
        Item("Apple", 2.5, 0.1),
        Item("Banana", 1.5, 0.2),
        Item("Orange", 3.0, 0.15),
        Item("Mango", 4.0, 0.3)
    ]
    
    cart = Cart()  # Create a Cart object
    
    while True:
        print("Available Items:")
        display_items(items)  # Display all available items
        choice = input("Enter the number of the item you want to add to the cart (or 'done' to finish): ")
        
        if choice.lower() == 'done':  # If user inputs 'done', exit the loop
            break
        
        try:
            choice = int(choice)  # Convert the user's choice to an integer
            if 1 <= choice <= len(items):  # Check if the choice is within the valid range
                item = items[choice-1]  # Get the selected item based on the user's choice
                new_weight = float(input(f"Enter the new weight for {item.name} (current weight: {item.weight} kg): "))
                item.update_weight(new_weight)  # Update the item's weight
                cart.add_item(item)  # Add the item to the cart
                print("Item added to cart.")
            else:
                print("Invalid item number.")  # Handle invalid item number
        except ValueError:
            print("Invalid input.")  # Handle invalid input
        
    print("\nItems in Cart:")
    display_items(cart.items)  # Display items currently in the cart
    print(f"\nTotal Price: ${cart.total_price()}")  # Print the total price of items in the cart
    
    while True:
        payment_choice = input("\nEnter '1' to confirm purchase, '2' to cancel, or any other key to use another payment method: ")
        
        if payment_choice == '1':  # If user confirms purchase
            print("Purchase successful!")  # Print success message
            break
        elif payment_choice == '2':  # If user cancels purchase
            print("Purchase canceled.")  # Print cancellation message
            break
        else:
            print("Invalid choice. Please try again.")  # Handle invalid payment choice

# Check if the script is run directly
if __name__ == "__main__":
    main()  # Call the main function to start the program