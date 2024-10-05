import turtle  # Import the turtle module for creating graphics

# Set up the screen
wn = turtle.Screen()         # Create a screen object
wn.title("Turtle Square")    # Set the title of the window to "Turtle Square"
wn.bgcolor("lightblue")      # Set the background color of the window to light blue

# Set up the turtle
t = turtle.Turtle()          # Create a turtle object
t.color("black")             # Set the color of the turtle to black
t.speed(2)                   # Set the speed of the turtle to 2 (medium speed)

# Draw a square
for _ in range(4):           # Loop 4 times to create the four sides of the square
    t.forward(100)           # Move the turtle forward by 100 units
    t.left(90)               # Turn the turtle left by 90 degrees

# Keep the window open until the user closes it
wn.mainloop()                # Enter the main loop, which keeps the window open