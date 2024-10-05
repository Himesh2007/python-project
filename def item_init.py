# Define a function to initialize an item with name, price, and weight
def item_init(name, price, weight):
    # Return a dictionary representing the item
    return {"name": name, "price": price, "weight": weight}

# Define a function to create a string representation of an item
def item_str(item):
    # Format the item information as a string
    return f"{item['name']} - Price: ${item['price']}, Weight: {item['weight']} kg"

# Define a function to update the weight of an item and adjust its price accordingly
def update_weight(item, new_weight):
    if new_weight < item['weight']:
        # Decrease in weight, adjust price proportionally
        item['price'] *= (new_weight / item['weight'])
    else:
        # Increase in weight, adjust price proportionally
        item['price'] *= (new_weight / item['weight'])
    # Update the item's weight to the new weight
    item['weight'] = new_weight

# Define a function to display a list of items
def display_items(items):
    for i, item in enumerate(items):
        # Print each item's information with its index
        print(f"{i+1}. {item_str(item)}")

# Define the main shopping function
def shopping():
    # Initialize a list of available items
    items = [
        item_init("Apple", 2.5, 0.1),
        item_init("Banana", 1.5, 0.2),
        item_init("Orange", 3.0, 0.15),
        item_init("Mango", 4.0, 0.3)
    ]
    # Initialize an empty cart
    cart = []
    
    while True:
        # Display available items to the user
        print("Available Items:")
        display_items(items)
        
        # Prompt the user to choose an item or finish shopping
        choice = input("Enter the number of the item you want to add to the cart (or 'done' to finish): ")
        
        if choice.lower() == 'done':
            # Exit the loop if the user is done
            break
        
        try:
            # Convert the choice to an integer
            choice = int(choice)
            
            if 1 <= choice <= len(items):
                # If the choice is valid, get the selected item
                item = items[choice - 1]
                
                # Prompt the user for the new weight
                new_weight = float(input(f"Enter the new weight for {item['name']} (current weight: {item['weight']} kg): "))
                
                # Update the item's weight and price
                update_weight(item, new_weight)
                
                # Add the item to the cart
                cart.append(item)
                print("Item added to cart.")
            else:
                print("Invalid item number.")
        
        except ValueError:
            # Handle invalid input (non-integer or non-float)
            print("Invalid input.")
    
    # Display items in the cart
    print("\nItems in Cart:")
    display_items(cart)
    
    # Calculate the total price of items in the cart
    total_price = sum(item['price'] for item in cart)
    print(f"\nTotal Price: ${total_price}")
    
    while True:
        # Prompt the user for payment confirmation
        payment_choice = input("\nEnter '1' to confirm purchase, '2' to cancel, or any other key to use another payment method: ")
        
        if payment_choice == '1':
            # Confirm the purchase
            print("Purchase successful!")
            break
        elif payment_choice == '2':
            # Cancel the purchase
            print("Purchase canceled.")
            break
        else:
            # Handle invalid payment choice
            print("Invalid choice. Please try again.")

# Call the shopping function to start the process
shopping()