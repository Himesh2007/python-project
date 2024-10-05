# Define a class 'car' with attributes and a method
class car:
    # Class attributes
    color = "white"       # Default color of the car
    wheel = 4            # Number of wheels
    speed = "298km/hr"   # Speed of the car
    sit = 4              # Number of seats

    # Method to start the car
    def start(self):
        print("car started")

# Create an instance of the 'car' class named 'bmw'
bmw = car()

# Print the 'bmw' instance
print(bmw)  # This prints the memory address of the 'bmw' object by default

# Create another instance of the 'car' class named 'ferrari'
ferrari = car()

# Modify the 'color' attribute of the 'ferrari' instance
ferrari.color = "blue"

# Print the 'color' attribute of the 'ferrari' instance
print(ferrari.color)  # This prints "blue"

# Call the 'start' method on the 'bmw' instance
bmw.start()  # This prints "car started"

# Call the 'start' method on the 'ferrari' instance
ferrari.start()  # This prints "car started"