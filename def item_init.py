def item_init(name, price, weight):
     return {"name": name, "price": price, "weight": weight}
def item_str(item):
     return f"{item['name']} - Price: ${item['price']}, Weight: {item['weight']} kg"
def update_weight(item, new_weight):
     if new_weight < item['weight']:
         item['price'] *= (new_weight / item['weight'])
         item['weight'] = new_weight
     else:
         item['price'] = item['price'] * (new_weight / item['weight'])
         item['weight'] = new_weight
def display_items(items):
     for i, item in enumerate(items):
         print(f"{i+1}. {item_str(item)}")
def shopping():
     items = [
         item_init("Apple", 2.5, 0.1),
         item_init("Banana", 1.5, 0.2),
         item_init("Orange", 3.0, 0.15),
         item_init("Mango", 4.0, 0.3)
     ]
     cart = []
     while True:
         print("Available Items:")
         display_items(items)
         choice = input("Enter the number of the item you want to add to the cart (or 'done' to finish): ")
         if choice.lower() == 'done':
             break
         try:
             choice = int(choice)
             if 1 <= choice <= len(items):
                 item = items[choice-1]
                 new_weight = float(input(f"Enter the new weight for {item['name']} (current weight: {item['weight']} kg): "))
                 update_weight(item, new_weight)
                 cart.append(item)
                 print("Item added to cart.")
             else:
                 print("Invalid item number.")
         except ValueError:
             print("Invalid input.")
     print("\nItems in Cart:")
     display_items(cart)
     total_price = sum(item['price'] for item in cart)
     print(f"\nTotal Price: ${total_price}")
     while True:
         payment_choice = input("\nEnter '1' to confirm purchase, '2' to cancel, or any other key to use another payment method: ")
         if payment_choice == '1':
             print("Purchase successful!")
             break
         elif payment_choice == '2':
             print("Purchase canceled.")
             break
         else:
             print("Invalid choice. Please try again.")
shopping()