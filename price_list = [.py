class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight
    def str(self):
        return f"{self.name} - Price: ${self.price}, Weight: {self.weight} kg"
    def update_weight(self, new_weight):
        if new_weight < self.weight:
            self.price *= (new_weight / self.weight)
            self.weight = new_weight
        else:
            self.price = self.price * (new_weight / self.weight)
            self.weight = new_weight
class Cart:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def total_price(self):
        return sum(item.price for item in self.items)
def display_items(items):
    for i, item in enumerate(items):
        print(f"{i+1}. {item}")
def main():
    items = [
        Item("Apple", 2.5, 0.1),
        Item("Banana", 1.5, 0.2),
        Item("Orange", 3.0, 0.15),
        Item("Mango", 4.0, 0.3)
    ]
    cart = Cart()
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
                new_weight = float(input(f"Enter the new weight for {item.name} (current weight: {item.weight} kg): "))
                item.update_weight(new_weight)
                cart.add_item(item)
                print("Item added to cart.")
            else:
                print("Invalid item number.")
        except ValueError:
            print("Invalid input.")
    print("\nItems in Cart:")
    display_items(cart.items)
    print(f"\nTotal Price: ${cart.total_price()}")
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
if __name__ == "__main__":
    main()