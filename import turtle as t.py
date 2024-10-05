import random  # Import the random module for random number generation
import turtle  # Import the turtle module for turtle graphics

# Function to check if the turtle is within the screen bounds
def isInScreen(win, turt):
	leftBound = -win.window_width() / 2   # Calculate the left boundary
	rightBound = win.window_width() / 2   # Calculate the right boundary
	topBound = win.window_height() / 2    # Calculate the top boundary
	bottomBound = -win.window_height() / 2  # Calculate the bottom boundary
	turtleX = turt.xcor()   # Get the turtle's x-coordinate
	turtleY = turt.ycor()   # Get the turtle's y-coordinate
	stillIn = True   # Initialize a flag to check if the turtle is still in bounds
	if turtleX > rightBound or turtleX < leftBound:  # Check if the turtle is out of horizontal bounds
		stillIn = False
	if turtleY > topBound or turtleY < bottomBound:  # Check if the turtle is out of vertical bounds
		stillIn = False
	return stillIn  # Return the flag

# Function to check if two turtles are in the same position
def sameposition(Red, Blue):
	if Red.pos() == Blue.pos():  # Compare the positions of the two turtles
		return False  # If they are in the same position, return False
	else:
		return True  # If they are in different positions, return True

# Main function to run the turtle race
def main():
	wn = turtle.Screen()  # Create a screen object
	Red = turtle.Turtle()  # Create a red turtle object
	Red.pencolor("red")  # Set the red turtle's pen color to red
	Red.pensize(5)  # Set the red turtle's pen size to 5
	Red.shape('turtle')  # Set the red turtle's shape to 'turtle'
	pos = Red.pos()  # Get the initial position of the red turtle
	Blue = turtle.Turtle()  # Create a blue turtle object
	Blue.pencolor("blue")  # Set the blue turtle's pen color to blue
	Blue.pensize(5)  # Set the blue turtle's pen size to 5
	Blue.shape('turtle')  # Set the blue turtle's shape to 'turtle'
	Blue.hideturtle()  # Hide the blue turtle initially
	Blue.penup()  # Lift the pen of the blue turtle to move without drawing
	Blue.goto(pos[0] + 50, pos[1])  # Move the blue turtle to a position 50 units to the right of the red turtle
	Blue.showturtle()  # Show the blue turtle
	Blue.pendown()  # Lower the pen of the blue turtle to start drawing
	mT = True  # Initialize the flag for the blue turtle being in bounds
	jT = True  # Initialize the flag for the red turtle being in bounds
	while mT and jT and sameposition(Red, Blue):  # Continue the loop while both turtles are in bounds and not in the same position
		coinRed = random.randrange(0, 2)  # Randomly choose 0 or 1 for the red turtle
		angleRed = 90  # Set the angle to 90 degrees
		if coinRed == 0:  # If the coin is 0, turn the red turtle left
			Red.left(angleRed)
		else:  # If the coin is 1, turn the red turtle right
			Red.right(angleRed)
		coinBlue = random.randrange(0, 2)  # Randomly choose 0 or 1 for the blue turtle
		angleBlue = 90  # Set the angle to 90 degrees
		if coinBlue == 0:  # If the coin is 0, turn the blue turtle left
			Blue.left(angleBlue)
		else:  # If the coin is 1, turn the blue turtle right
			Blue.right(angleBlue)
		Red.forward(50)  # Move the red turtle forward by 50 units
		Blue.forward(50)  # Move the blue turtle forward by 50 units
		mT = isInScreen(wn, Blue)  # Check if the blue turtle is still in bounds
		jT = isInScreen(wn, Red)  # Check if the red turtle is still in bounds
	Red.pencolor("black")  # Set the red turtle's pen color to black
	Blue.pencolor("black")  # Set the blue turtle's pen color to black
	if jT and not mT:  # If the red turtle is in bounds and the blue turtle is not
		Red.write("Red Won", True, align="center", font=("arial", 15, "bold"))  # Write "Red Won" with the red turtle
	elif mT and not jT:  # If the blue turtle is in bounds and the red turtle is not
		Blue.write("Blue Won", True, align="center", font=("arial", 15, "bold"))  # Write "Blue Won" with the blue turtle
	else:  # If both turtles are either in bounds or out of bounds
		Red.write("Draw", True, align="center", font=("arial", 15, "bold"))  # Write "Draw" with the red turtle
		Blue.write("Draw", True, align="center", font=("arial", 15, "bold"))  # Write "Draw" with the blue turtle
	wn.exitonclick()  # Wait for the user to click on the window to close it

# Call the main function to start the program
main()